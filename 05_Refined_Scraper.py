# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 01:56:01 2021

@author: FAKENAME
"""

from Web_Scraper.Web_Scraper_Class import *


all_access_data_dict = {
    
    "The_Economist":{
        "site name": "The_Economist",
        "start page": "https://www.economist.com/",
        "storage path": "C:/Data/Web Scraper/The_Economist",
        "site map addr": "https://www.economist.com/sitemap.xml",
        "res loc dict": {
            "Title": {"tag":["span"], "attr":{"data-test-id":"Article Headline", "itemprop":"headline", "class":"article__headline"}, "keep":"all"},
            "Subtitle": {"tag":["span"], "attr":{"data-test-id":"Article Subheadline", "class":"article__subheadline"}, "keep":"all"},
            "Section": {"tag":["span"], "attr":{"class": "article__section-headline"}, "keep":"all"},
            "Author": {"tag":["p"], "attr":{"class": "article__byline", "itemprop":"byline"}, "keep":"all"},
            "Description": {"tag":["h2"], "attr":{"data-test-id":"Article Description", "itemprop":"description", "class":"article__description"}, "keep":0},
            "Location": {"tag":["p"], "attr":{"class":"article__dateline-location"}, "keep":"all"},
            "Date": {"tag":["time"], "attr":{"itemtype":"http://schema.org/DateTime", "class":"article__dateline-datetime"}, "keep":"time"},
            "Article": {"tag":["p"], "attr":{"class": "article__body-text"}, "keep":"all"}
            }
        },  
    
    "The_Spectator":{
        "site name": "The_Spectator",
        "start page": "https://www.spectator.co.uk/",
        "storage path": "C:/Data/Web Scraper/The_Spectator",
        "site map addr": "https://www.spectator.co.uk/sitemap.xml",
        "res loc dict": {
            "Title": {"tag":["h1"], "attr":{ "class":"ContentPageTitle-module__headline"}, "keep":"all"},
            "Subtitle": {"tag":["span"], "attr":{"data-test-id":"Article Subheadline", "class":"article__subheadline"}, "keep":"all"},
            "Section": {"tag":["span"], "attr":{"itemprop":"item"}, "keep":"all"},
            "Author": {"tag":["h2"], "attr":{"class": "ContentPageAuthor"}, "keep":"all"},
            "Description": {"tag":["h2"], "attr":{"data-test-id":"Article Description", "itemprop":"description", "class":"article__description"}, "keep":"all"},
            "Location": {"tag":["p"], "attr":{"class":"article__dateline-location"}, "keep":"all"},
            "Date": {"tag":["time"], "attr":{"class":"ContentPageMetadataItem-module__item"}, "keep":"all"},
            "Article": {"tag":["p"], "attr":{"class": "ContentPageBodyParagraph"}, "keep":"all"}
            }
        
        },    
    
    "Wired":{
        "site name": "Wired",
        "start page": "https://www.wired.co.uk/",
        "storage path": "C:/Data/Web Scraper/Wired",
        "site map addr": "https://www.wired.co.uk/sitemap.xml",
        "res loc dict": {
            "Title": {"tag":["h1"], "attr":{"class":"content-header__row content-header__hed", "data-testid":"ContentHeaderHed"}, "keep":"all"},
            "Subtitle": {"tag":["span"], "attr":{"data-test-id":"Article Subheadline", "class":"article__subheadline"}, "keep":"all"},
            "Section": {"tag":["div"], "attr":{"class": "content-header__rubric rubric-vertical-align"}, "keep":"all"},
            "Author": {"tag":["a"], "attr":{"class": "byline__name",}, "keep":0},
            "Description": {"tag":["div"], "attr":{"class":"content-header__row content-header__dek"}, "keep":"all"},
            "Location": {"tag":["p"], "attr":{"class":"article__dateline-location"}, "keep":"all"},
            "Date": {"tag":["time"], "attr":{"class":"content-header__publish-date"}, "keep":"all"},
            "Article": {"tag":["div"], "attr":{"class":"article__body"}, "keep":"all"}
            }
        
        },

    "Vogue_UK":{
        "site name": "Vogue_UK",
        "start page": "https://www.vogue.co.uk/",
        "storage path": "C:/Data/Web Scraper/VogueUK",
        "site map addr": "https://www.vogue.co.uk/sitemap.xml",
        "res loc dict": {
            "Title": {"tag":["h1"], "attr":{"class":"split-screen-content-header__hed"}, "keep":"all"},
            "Subtitle": {"tag":["span"], "attr":{"class":"sc-dHMioH gqLUkO"}, "keep":"all"},
            "Section": {"tag":["span"], "attr":{"class": "sc-pNWdM sc-jrsJWt sc-dPaNzc lfZoIg iLGJJd fqbJCS"}, "keep":"array"},
            "Author": {"tag":["a"], "attr":{"class": "byline__name",}, "keep":0},
            "Description": {"tag":["div"], "attr":{"class":"content-header__row content-header__dek"}, "keep":"all"},
            "Location": {"tag":["p"], "attr":{"class":"article__dateline-location"}, "keep":"all"},
            "Date": {"tag":["time"], "attr":{"class":"content-header__publish-date"}, "keep":"all"},
            "Article": {"tag":["div"], "attr":{"class":"grid--item body body__container article__body grid-layout__content","data-journey-hook":"client-content"}, "keep":"all"}
            }
        
        },  
   
    }

 
if __name__ == '__main__':
    
    current_site_dict = all_access_data_dict["Vogue_UK"] 
    
    # Setup the class instance
    s = news_web_scraper(data_storage_path = current_site_dict["storage path"],
                    start_page = current_site_dict["start page"],
                    site_name = current_site_dict["site name"],
                    resource_locator_dict = current_site_dict["res loc dict"],
                    DEBUG = False)
    
    # Get all article urls from the sitemap
    s.site_map_traversal(current_site_dict["site map addr"])
    
    # Extract one page
    # s.struc_html_data_extract("https://www.economist.com/europe/2021/06/24/french-voters-punish-presidential-poll-favourites")
    
    # While there are links that haven't been looked at, keep downloading
    while(len(s.urls_to_visit_dict) > 0):
        s.site_traversal(3000)
        s.new_output_JSON_for_Articles()
    

    
### TODO:
    
    # Rewrite the code to use external dependancies 
    
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
    