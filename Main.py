# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 01:56:01 2021

@author: FAKENAME
"""

import Web_Scraper.Web_Scraper_Class as webscraper
import Web_Scraper.Access_Vars as var

 
if __name__ == '__main__':
    
    current_site_dict = var.site_res_access_dict["Rolling_Stone"] 
    
    # Setup the class instance
    s = webscraper.news_web_scraper(data_storage_path = current_site_dict["storage path"],
                    start_page = current_site_dict["start page"],
                    site_name = current_site_dict["site name"],
                    resource_locator_dict = current_site_dict["res loc dict"],
                    DEBUG = False)
    
    # Get all article urls from the sitemap
    s.site_map_traversal(current_site_dict["site map addr"])
    
    # Extract one page
    # s.struc_html_data_extract("https://www.theatlantic.com/science/archive/2021/07/space-billionaires-jeff-bezos-richard-branson/619383/")
    
    # While there are links that haven't been looked at, keep downloading
    
    while(len(s.urls_to_visit_dict) > 0 or (s.last_visited_page == None)):
        s.site_traversal(3000)
        s.new_output_JSON_for_Articles()
    
    
    
    
    
### TODO:
    
    # Create a GUI interface in tkinter
    
    # Allow simultaneous downloads within the same process
    
    # Automate the creation of parts of the site_res_access_dict:
        # "site name"
        # "storage path"
    
    # Create a robots.txt parsing file to get the site map addresses and get restricted paths and stop them being accessed
    
    # Add random time to the page access delay (uniform between 0-1 sec)
    
    # 
 
    