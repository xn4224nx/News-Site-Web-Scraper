# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:02:58 2021

@author: FAKENAME
"""

site_res_access_dict = {
    
    "The_Economist":{
        "site name": "The_Economist",
        "start page": "https://www.economist.com/",
        "storage path": "D:/Data/Web Scraper/The_Economist",
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
        "storage path": "D:/Data/Web Scraper/The_Spectator",
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
        "storage path": "D:/Data/Web Scraper/Wired",
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
        "storage path": "D:/Data/Web Scraper/VogueUK",
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
    

    "National_Geographic":{
        "site name": "National_Geographic",
        "start page": "https://www.nationalgeographic.co.uk/",
        "storage path": "D:/Data/Web Scraper/national_geographic",
        "site map addr": "https://www.nationalgeographic.co.uk/sitemap/sitemap.xml",
        "res loc dict": {
            "Title": {"tag":["h1"], "attr":{"class":"css-1sgbwt8"}, "keep":"all"},
            "Subtitle": {"tag":["h2"], "attr":{"class":"css-ju6on1"}, "keep":"all"},
            "Section": {"tag":["div"], "attr":{"class": "css-gdhqwr"}, "keep":"all"},
            "Author": {"tag":["div"], "attr":{"class": "css-674bmm",}, "keep":0},
            "Description": {"tag":["div"], "attr":{"class":"ngart-img__cont__copy"}, "keep":0},
            "Location": {"tag":["p"], "attr":{"class":"article__dateline-location"}, "keep":"all"},
            "Date": {"tag":["span"], "attr":{"class":"css-1enp996"}, "keep":"all"},
            "Article": {"tag":["div"], "attr":{"class":"paragraph css-0"}, "keep":"all"}
            }
        
        },  
    
    "Rolling_Stone":{
        "site name": "Rolling_Stone",
        "start page": "https://www.rollingstone.com/",
        "storage path": "D:/Data/Web Scraper/Rolling_Stone",
        "site map addr": "https://www.nationalgeographic.co.uk/sitemap/sitemap.xml",
        "res loc dict": {
            "Title": {"tag":["h1"], "attr":{"class":"article-header__row"}, "keep":"all"},
            "Subtitle": {"tag":["h2"], "attr":{"class":"article-header__row"}, "keep":"all"},
            "Section": {"tag":["div"], "attr":{"class": "css-gdhqwr"}, "keep":"all"},
            "Author": {"tag":["h4"], "attr":{"class": "c-author__heading t-bold"}, "keep":0},
            "Description": {"tag":["div"], "attr":{"class":"ngart-img__cont__copy"}, "keep":0},
            "Location": {"tag":["p"], "attr":{"class":"article__dateline-location"}, "keep":"all"},
            "Date": {"tag":["time"], "attr":{"class":"time"}, "keep":"time"},
            "Article": {"tag":["div"], "attr":{"class":"l-article-content"}, "keep":"all"}
            }
        
        }, 
   
    }