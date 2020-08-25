# Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import time


def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser ('chrome', **executable_path, headless=False)

mars_data = {}

# URL of page to be scraped

def scrape():
    # Initialize browser 
    browser = init_browser()

    nasa_url = 'https://mars.nasa.gov/news/'

    browser.visit(nasa_url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    html = browser.html

    soup = bs(html, 'html.parser')

    news_title = soup.find('div', class_='content_title').get_text()
    news_p = soup.find('div', class_='article_teaser_body').get_text()

 
    mars_data['news_title'] = news_title
    mars_data['news_paragraph'] = news_p
    

    # Image -  Visit jpl.com
    jpl_url = 'https://www.jpl.nasa.gov'
    jpl_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars#submit'
    
    browser.visit(jpl_image_url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
    
        # Scrape page into Soup
    html = browser.html
    jpl_soup = bs(html, "html.parser")

    relative_image_path = jpl_soup.find_all('a', class_='button fancybox')[0].get('data-fancybox-href').strip()
    featured_image_url = jpl_url + relative_image_path
    mars_data['featured_image_url'] = featured_image_url 
     
    # Mars Facts
    mars_url = 'https://space-facts.com/mars/'
    browser.visit(mars_url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
        
    tables = pd.read_html(mars_url)
    mars_df = tables[0]
    mars_df.columns = ['Variable', 'Description']
    html_table = mars_df.to_html()

    mars_data['mars_df'] = html_table


    # Hemispheres - Visit USGS website
    hemis_url = 'https://astrogeology.usgs.gov'
    hemis_img_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemis_img_url)
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

        # Scrape with beautiful soup
    html = browser.html
    soup = bs(html, 'html.parser')
    results = soup.find_all('div', class_='item')

        # Create empty list 
    hemis_list = []

        # Loop through the results
    for result in results: 
        title = result.find('h3').text
        img_url = result.find('a', class_='itemLink product-item')['href']
        browser.visit(hemis_url + img_url)
        img_html = browser.html
    
        soup = bs(img_html, 'html.parser')
        img_url = hemis_url + soup.find('img', class_='wide-image')['src']
    
        # Append the information into list  
        hemis_list.append({"title" : title, "img_url" : img_url})

    mars_data['hemis_list'] = hemis_list       
    browser.quit()
    return mars_data


