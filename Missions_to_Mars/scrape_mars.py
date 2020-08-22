#!/usr/bin/env python
# coding: utf-8

# # Web Scraping Homework - Mission to Mars

# In[1]:


# Dependencies
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import time


# In[2]:

def init_browser():
# Path
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


# ## NASA Mars News

# In[9]:


# URL of page to be scraped
nasa_url = 'https://mars.nasa.gov/news/'


# In[10]:

def scrape_info():
    browser.visit(nasa_url)


html = browser.html


# In[11]:


time.sleep(10)


# In[12]:


soup = bs(html, 'html.parser')


# In[13]:


news = soup.find('ul', class_='item_list')


# In[14]:


news_title = news.find('div', class_='content_title').find('a').text
news_p = news.find('div', class_='article_teaser_body').text


# In[15]:


# # Print results
#             print('-------------------------------------------------------------------------')
#             print('news_title = "',news_title,'"')
#             print('news_p =','"',news_p,'"')
#             print('-------------------------------------------------------------------------')


# ## JPL Mars Space Images - Featured Image

# In[16]:


# Visit jpl.com
jpl_url = 'https://www.jpl.nasa.gov/'
jpl_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(jpl_image_url)


# In[17]:


time.sleep(1)


# In[18]:


# Scrape page into Soup
html = browser.html
soup = bs(html, "html.parser")


# In[19]:


# Find the src for the jpl image
relative_image_path = soup.find_all('a', class_='button fancybox')[0].get('data-fancybox-href').strip()
featured_image_url = jpl_url + relative_image_path
# print(f"featured_image_url: {featured_image_url}")


# # Mars Facts

# In[20]:


# Visit jpl.com
mars_url = 'https://space-facts.com/mars/'
browser.visit(mars_url)


# In[21]:


tables = pd.read_html(mars_url)
tables


# In[22]:


mars_df = tables[0]
mars_df.columns = ['Variable', 'Description']
mars_df.head(10)


# In[23]:


html_table = mars_df.to_html()
html_table


# In[24]:


html_table.replace('\n', '')


# In[25]:


print(html_table)


# # Mars Hemispheres

# In[26]:


#Visit USGS website
hemis_url = 'https://astrogeology.usgs.gov'
hemis_img_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemis_img_url)


# In[27]:


# Scrape with beautiful soup
html = browser.html
soup = bs(html, 'html.parser')
results = soup.find_all('div', class_='item')


# In[28]:


# Create empty list 
hemis_list = []

# Loop through the results
for result in results: 
    title = result.find('h3').text
    img_url = result.find('a')['href']
    browser.visit(hemis_url + img_url)
    img_html = browser.html
    
    soup = bs(img_html, 'html.parser')
    img_url = hemis_url + soup.find('img', class_='wide-image')['src']
    
    # Append the information into list  
    hemis_list.append({"title" : title, "img_url" : img_url})
hemis_list

    # Store data in a dictionary
    mars_data = {
        "news title": news_title,
        "news": news_P,
        "featured image": featured_image_url,
        "mars data table": html_table,        
        "hemisphere image": hemis_list   

    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
    
    
   