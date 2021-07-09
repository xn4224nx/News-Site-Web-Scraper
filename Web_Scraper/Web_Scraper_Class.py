# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 14:21:48 2021

@author: FAKENAME
"""

import requests, re, os, json, random, time, collections
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from datetime import datetime, timedelta
import Web_Scraper.Scrap_Aux_Functions as aux


class news_web_scraper:
    def __init__(self, data_storage_path, start_page, site_name, resource_locator_dict,  DEBUG = False):
    
        # Website infomation
        self.start_page = start_page
        self.urls_to_scrape = None
        self.site_name = site_name
        self.base_url = '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(self.start_page))
        self.resource_locator_dict = resource_locator_dict
        self.last_visited_page = None
        self.last_visited_article = None
        self.time_started = None
        
        self.access_time_deque = collections.deque([])
        self.access_time_deque_limit = 1000
        
        # Site text JSON Storage Info
        self.data_storage_path = os.path.abspath(data_storage_path)
        self.main_JSON_path = None
        self.old_web_data = {}
        
        # Site URL Storage Paths
        self.all_visited_urls_path = None
        self.all_saved_urls_path = None
        self.urls_to_visit_path = None
        
        # Site URL Storage Object
        self.all_visited_urls_dict = {}
        self.all_saved_urls_dict = {}
        self.urls_to_visit_dict = {}
        
        # System Variables
        self.DEBUG = DEBUG
        self.request_delay = 3
        self.X_Forwarded_For = "66.102.0.0"
        self.User_Agent = "Googlebot-News"
        self.scrape_header = {
                                "UserHostAddress": 	"162.158.111.110",
                                "UserHostName": 	"162.158.111.110",
                                "IsSecureConnection": 	"True",
                                "IsAuthenticated": 	"False",
                                "Connection": 	"Keep-Alive",
                                "Accept": 	"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                                "Accept-Encoding": 	"gzip",
                                "Accept-Language":	"en-GB,en;q=0.5",
                                "Referer": 	"https://www.google.com/",
                                "User-Agent": 	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
                                "X-Forwarded-For": 	"213.31.18.164",
                                "X-Forwarded-Proto": 	"https",
                              }
        
        # Catch no directory given
        if not os.path.isdir(self.data_storage_path):
            print("Error Directory: " + self.data_storage_path + "\n\tDoesn't exist.")
            os.makedirs(self.data_storage_path)
            print("\tFolder created")

        
        # Create a new JSON File
        file_name = self.site_name + datetime.now().strftime("_%Y_%m_%d-%H%M%S") + ".JSON"
        path = os.path.join(self.data_storage_path, file_name)
        with open(path, "w") as f:
            f.write("{}")
        
        # Set the path to the main JSON storage file
        self.main_JSON_path = os.path.join(self.data_storage_path, file_name)
        
        if self.DEBUG:
            print("The filename is: "+ file_name)
            print("The full path is: \n\t"+ self.main_JSON_path, end="\n\n\n")
               
 
        
        # Check storage paths
        self.all_visited_urls_path = os.path.join(self.data_storage_path, self.site_name + "_Visited_URLs" + ".JSON")
        self.all_saved_urls_path = os.path.join(self.data_storage_path, self.site_name + "_Saved_URLs" + ".JSON")
        self.urls_to_visit_path = os.path.join(self.data_storage_path, self.site_name + "_URLs_to_Visit" + ".JSON")
        
        # Create files if they don't exist
        if (not os.path.exists(self.all_visited_urls_path)):
            with open(self.all_visited_urls_path, "w") as f:
                f.write("{}")
        else:
            with open(self.all_visited_urls_path, 'r') as json_file:
                self.all_visited_urls_dict = json.load(json_file)
            
        # Create files if they don't exist
        if (not os.path.exists(self.all_saved_urls_path)):
            with open(self.all_saved_urls_path, "w") as f:
                f.write("{}")
        else:
            with open(self.all_saved_urls_path, 'r') as json_file:
                self.all_saved_urls_dict = json.load(json_file)

        # Create files if they don't exist
        if (not os.path.exists(self.urls_to_visit_path)):
            with open(self.urls_to_visit_path, "w") as f:
                f.write("{}")
        else:
            with open(self.urls_to_visit_path, 'r') as json_file:
                self.urls_to_visit_dict = json.load(json_file)




    def site_traversal(self, scan_limit=3):
        self.scan_limit = scan_limit
        
        # Start from the homepage get the data check if the key is in self.old_web_data
        # Download the data and add it to the set of visited pages
        
        page_to_check = self.start_page
        new_pages_found = 0
        
        while(new_pages_found < scan_limit):
            
            # check you are connected to the internet
            if(not aux.is_connected_to_internet()): break
            
            # Skip a url if its been seen before
            if(page_to_check in self.all_visited_urls_dict):
                
                # Set the new page_to_check
                page_to_check = random.choice(list(self.urls_to_visit_dict.keys()))
                continue
            
            # Record the time that the particular loop iteration starts
            t_0 =  time.time()
               
            # Extract the data for the page_to_check
            data_dict, urls_on_page = self.struc_html_data_extract(page_to_check)
            
            self.last_visited_page = page_to_check 
                
            if self.DEBUG:
                print("\nData Downloaded from:\n\t" + page_to_check)
            
            # Find out if the page is in either all_visited_urls_dict or all_saved_urls_dict
            if page_to_check not in self.all_visited_urls_dict:
                self.all_visited_urls_dict[page_to_check] = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
            
            # Check if the page is viable for saving
            if (data_dict["Article"] != None) and (page_to_check not in self.all_saved_urls_dict):
                
                # Update counters & all found articles dict
                self.old_web_data[page_to_check] = data_dict
                new_pages_found += 1
                self.all_saved_urls_dict[page_to_check] = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
                
                if self.DEBUG:
                    print("New article found:\n\t" + page_to_check, end = "\n\n")
                
                self.last_visited_article = page_to_check 
            
            # Add the found urls to the set of URLS's to scrape          
            for url in urls_on_page:
                if url not in self.urls_to_visit_dict:
                    self.urls_to_visit_dict[url] = None

            # Remove URLS that have been seen before
            for url in self.all_visited_urls_dict:
                if url in self.urls_to_visit_dict:
                    self.urls_to_visit_dict.pop(url)
            
            # Save all the JSONS
            self.save_all_JSONs()
                
            # Set the new page_to_check
            if list(self.urls_to_visit_dict.keys()):
                page_to_check = random.choice(list(self.urls_to_visit_dict.keys()))
            else:
                # If there are no pages to check, break the loop
                print("\n\nNo pages found to check\n\n")
                break
            
            # Record the time that the particular loop iteration ends
            loop_time_length = time.time() - t_0
            
            # Append the time a loop takes to the deque
            if(loop_time_length > self.request_delay):             
                self.access_time_deque.append(loop_time_length)
                
            else:
                self.access_time_deque.append(self.request_delay)
            
            # if there are more than the limit remove old times
            if (len(self.access_time_deque) > self.access_time_deque_limit):
                self.access_time_deque.popleft()

            self.print_trawler_progress()
            
            # If less seconds have passed than the request delay make sure the
            # full delay is completed.
            if (loop_time_length < self.request_delay):
                time.sleep(self.request_delay - (loop_time_length))
 



    def struc_html_data_extract(self, page_url):
        """
        Get a html page and extact all the links and visible text
        with infomation about what tag they are assoicated with and the
        class info and put it into a dict
        """
        
        return_dict = {}
        all_href_on_page = [] 
        
        # Create the return dict from the keys in the resource_locator_dict
        for key in self.resource_locator_dict:
             return_dict[key] = None
        
        # Get the raw html
        try:
            raw_request = requests.get(page_url , headers = self.scrape_header)
        
        except:
            # If the request fails return blank data
            if self.DEBUG:
                print("\n\nPage Extract Failed:\n\t" + page_url + "\n\n")
                
            return return_dict, all_href_on_page  
        
        # Parse the HTML
        soup = BeautifulSoup(raw_request.content, 'html.parser')
        
        
        #### Extract all the links on the page
        for ahref_block in soup.find_all('a'):

            link = ahref_block.get('href')

            # Don't process links that are empty or external
            if link is None:
                continue
            

            # Detect incomplete urls and try and make them usable
            if not link.startswith('http'):
                link = urljoin(self.base_url, link)
          
            # # Remove external links     
            # if link_base_url not in self.base_url:
            #     continue

            # Remove anchor data from any url
            if '#' in link:
                head, sep, tail = link.partition('#')
                link = head

            # Remove external links     
            if self.base_url not in link:
                continue
            
            #Save the good urls
            all_href_on_page.append(link)
        
        # Remove duplicate links
        return_urls = list(set(all_href_on_page))
            
        #### Extract the key pieces of text according to resource_locator_dict
        for res_name, res_access_dict in self.resource_locator_dict.items():
            
            temp = []
            regex_attr_dict = {}
            
            if "attr" in res_access_dict:
                # Create Regex for the attr dict
                for attr_name in res_access_dict["attr"]:
                    regex_attr_dict[attr_name] = re.compile('.*'+str(res_access_dict["attr"][attr_name])+'.*')
            
            # Extract all the HTML associated with that tag & attributes
            arr_of_html_blocks = soup.find_all(res_access_dict["tag"], 
                                        attrs=regex_attr_dict)
            
            # Extract infomation based on the "keep" item
            
            # Extract all text
            if(res_access_dict["keep"] in ["all", "array"]):
                
                # Get all text into an array
                for block in arr_of_html_blocks:
                    temp.append(block.get_text())
                
                if(res_access_dict["keep"] == "all"):
                    # Put all the element of the array into one string seperated by a space
                    temp = ' '.join(temp)
                
                # If the string is blank set it as None
                if temp == '':
                    temp = None
            
            # Save a certain bit of info at a int position 
            elif(isinstance(res_access_dict["keep"], int)):
                try:
                    temp = arr_of_html_blocks[res_access_dict["keep"]].get_text()
                except:
                    temp = None
                
            # Save Time Data
            elif(res_access_dict["keep"] == "time"):
                for block in arr_of_html_blocks:
                    if block.has_attr("datetime"):
                        temp = block['datetime']
                        break
            
            # Save part of the URL
            elif(res_access_dict["keep"] == "URL"):
                temp = aux.extract_string(page_url, res_access_dict["attr"]["pre"], res_access_dict["attr"]["post"])
            
            # Catch the which not being a valid type
            else:
                print("Which type of: '"+str(res_access_dict["keep"])+"' is unknown.")
                raise ValueError
            
            # Put the saved info into the return dict
            return_dict[res_name] = aux.remove_non_ascii(temp)
        
        if self.DEBUG:                    
            for res_name, res_results in return_dict.items():
                
                print(res_name, end = "\n\n")
                print(res_results, end = "\n\n\n")
        
        return return_dict, return_urls                 
       


    def site_map_traversal(self, site_map_xml):
        
        # Extract all html from the site map xml and the sub xmls and add all
        # the found htmls to `self.urls_to_visit_dict`
        
        # Key Variables
        all_found_xmls_dict = {site_map_xml : None}
        all_found_htmls_dict = {}
        cur_xml_page = site_map_xml
        
        # Get all the xml & html in sub xml pages
        while(None in all_found_xmls_dict.values()):
            
            # Record the time that the particular loop iteration starts
            t_0 =  time.time()
            
            # Extract all html & xml from the cur_xml_page
            found_xmls_dict, found_htmls_dict = self.site_map_extract(cur_xml_page)
            
            # Add the found links to the relevant dicts
            all_found_xmls_dict.update(found_xmls_dict)
            all_found_htmls_dict.update(found_htmls_dict)
            
            # Add the found html files to `urls_to_visit_dict`
            self.urls_to_visit_dict.update(all_found_htmls_dict)
            
            # Mark the previously scraped xml link as checked
            all_found_xmls_dict[cur_xml_page] = True
            
            # Find a new xml link to check next
            possible_xml_to_check_next = [k for k,v in all_found_xmls_dict.items() if v == None]
            
            # Break if none are found
            if possible_xml_to_check_next:
                cur_xml_page = random.choice(possible_xml_to_check_next)
            else:
                break 
            
            # Record the time that the particular loop iteration ends
            loop_time_length = time.time() - t_0
            
            # If less seconds have passed than the request delay make sure the
            # full delay is completed.
            if (loop_time_length < self.request_delay):
                time.sleep(self.request_delay - (loop_time_length))
 
        # Print infomation about what has been found
        print("\n\nIn the site: "+ site_map_xml)
        print("\t" + str(len(all_found_xmls_dict)-1) +" XML files have been found in total and")
        print("\t" + str(len(all_found_htmls_dict)) +" HTML files have been found in total", end = "\n\n")
        
        # Save all the JSONS
        self.save_all_JSONs()
        

    
    def site_map_extract(self, xml_address):
        
        found_xmls_dict = {}
        found_htmls_dict = {}
    
        # get the xml map
        xml_map = requests.get(xml_address, headers = self.scrape_header)
        soup = BeautifulSoup(xml_map.text,'lxml')
        
        # Get all the xml and html links on the sitemap xml page
        sitemapTags = soup.find_all("loc")
        
        for sitemap in sitemapTags:
            
            # Extract the addresses
            address = sitemap.text
            
            # Get the XML link
            if ".xml" in address:
                found_xmls_dict[address] = None 
                if self.DEBUG:
                    print(address)

            # Get the HTML link
            else:
                found_htmls_dict[address] = None
                if self.DEBUG:
                    print(address)    
                    
        if self.DEBUG:
            print("\n\nOn the page: " + xml_address)   
            print("\t" + str(len(found_xmls_dict)) +" XML pages found")
            print("\t" + str(len(found_htmls_dict)) +" HTML pages found\n\n")
        
        return found_xmls_dict, found_htmls_dict


    
    def print_trawler_progress(self):
        """
        Print the webcrawler progress also updates itself
        """
        
        # Completion time based on the average time to process a page
        
        avg_time_process_page = sum(list(self.access_time_deque)) / len(self.access_time_deque)
        completed_datetime = datetime.now() + timedelta(seconds=avg_time_process_page * len(self.urls_to_visit_dict))
        
        visited_pages = "Site: {:20s}\n\tLast Visited Page:    {:20s}\n\tLast Visited Article: {:20s}\n\n".format(
            self.base_url,
            str(self.last_visited_page),
            str(self.last_visited_article)
            )
        
        crawler_stats = "Overall Progress Stats\n\tPages Visited:  {:>5d}\n\tPages to Visit: {:>5d}\n\tArticles Found: {:>5d}\n\n".format(
            len(self.all_visited_urls_dict),
            len(self.urls_to_visit_dict),
            len(self.all_saved_urls_dict)            
            
            )
        
        time_stats = "Estimated Time Statistics\n\tEstimated Time of Completion: {:30}\n\tAverage time to process a page: {:3.2f}\n\n".format(
            completed_datetime.strftime("%c"),
            avg_time_process_page
            )
        
        print(visited_pages + crawler_stats + time_stats +"+"*30, end = "\n\n")



    def new_output_JSON_for_Articles(self):
        
        # Make sure the old web data is saved to the old filepath
        with open(self.main_JSON_path, 'w+') as f:
            json.dump(self.old_web_data, f, indent=4)
        
        # Create a new JSON File
        file_name = self.site_name + datetime.now().strftime("_%Y_%m_%d-%H%M%S") + ".JSON"
        path = os.path.join(self.data_storage_path, file_name)
        
        if self.DEBUG:
            print("New path is: " + path)
        
        with open(path, "w") as f:
            f.write("{}")
        
        # Set the path to the main JSON storage file
        self.main_JSON_path = os.path.join(self.data_storage_path, file_name)
        
        # Clear old webdata
        self.old_web_data = {}         
    
    def save_all_JSONs(self):
        
        # Save the found articles
        with open(self.main_JSON_path, 'w+') as f:
            json.dump(self.old_web_data, f, indent=4)
        
        # Save the visitied URLs
        with open(self.all_visited_urls_path, 'w+') as f:
            json.dump(self.all_visited_urls_dict, f, indent=4)
        
        # Save the saved URLs
        with open(self.all_saved_urls_path, 'w+') as f:
            json.dump(self.all_saved_urls_dict, f, indent=4)
        
        # Save the URLs to visit
        with open(self.urls_to_visit_path, 'w+') as f:
            json.dump(self.urls_to_visit_dict, f, indent=4)        
    