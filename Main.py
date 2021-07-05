# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 01:56:01 2021

@author: FAKENAME
"""

import Web_Scraper.Web_Scraper_Class as webscraper
import Web_Scraper.Access_Vars as var

 
if __name__ == '__main__':
    
    current_site_dict = var.site_res_access_dict["National_Geographic"] 
    
    # Setup the class instance
    s = webscraper.news_web_scraper(data_storage_path = current_site_dict["storage path"],
                    start_page = current_site_dict["start page"],
                    site_name = current_site_dict["site name"],
                    resource_locator_dict = current_site_dict["res loc dict"],
                    DEBUG = True)
    
    # Get all article urls from the sitemap
    #s.site_map_traversal(current_site_dict["site map addr"])
    
    # Extract one page
    s.struc_html_data_extract("https://www.nationalgeographic.co.uk/animals/2021/07/sea-anemones-sometimes-eat-ants-but-why-and-how")
    
    # While there are links that haven't been looked at, keep downloading
    # while(len(s.urls_to_visit_dict) > 0):
    #     s.site_traversal(3000)
    #     s.new_output_JSON_for_Articles()
    
    
    
    
    
### TODO:
    
    # Create a GUI interface in tkinter
    
    # Rewrite the functions to be more flexible and work outside the economist site:

        # www.economist.com                 -- DONE
        # www.wired.co.uk                   -- DONE
        # www.spectator.co.uk               -- DONE
        # www.vogue.co.uk                   -- DONE
        # www.nationalgeographic.co.uk
        # www.rollingstone.com
        # www.newstatesman.com
        # www.theweek.co.uk
        # www.theatlantic.com

    # For each site:
        # Make a locator dict
        # Check the site map fn works
    
    # only save file when a new article is found so if the connection gets interupted
    
    # Change the program logic to end or pause if the internet is disconnected and try again
    # in a number of minutes/quit
    
    # Put the site access dict into another file (maybe a JSON or other type)
    
    # Adjust the displayed access time to be an average of the last 100 accesses
    # and thus use that for the finish datetime.
    