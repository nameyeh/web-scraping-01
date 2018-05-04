
# coding: utf-8

# # Step 1 - Scraping

# In[1]:


# Complete your initial scraping using 
# Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

# Create a Jupyter Notebook file called mission_to_mars.ipynb 
# and use this to complete all of your scraping and analysis tasks. 
# The following outlines what you need to scrape.


# ### NASA Mars News

# In[2]:


# Scrape the NASA Mars News Site and collect the latest News Title and Paragragh Text. 
# Assign the text to variables that you can reference later.
# # Example:
# news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

# news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer,\
# on course for launch next May from Vandenberg Air Force Base in central California -- the first\
# interplanetary launch in history from America's West Coast."


# In[34]:




def scrape():
    # Dependencies
    import time 
    import requests
    import pandas as pd
    from bs4 import BeautifulSoup
    from splinter import Browser
    # from selenium.webdriver.common import action_chains, keys
    # from selenium import webdriver
    import pymongo
    conn = "mongodb://localhost:27017"
    client = pymongo.MongoClient(conn)
    db = client.mars_db
    mars_data = db.mars_data
    db.mars_data.drop()

    output = {}
    # having issues with browser, use webdriver instead 
    
    #driver = webdriver.Chrome()
    #url = 'https://mars.nasa.gov/news/'
    #driver.get(url)
    
    #html = driver.page_source
    #soup = BeautifulSoup(html, 'lxml')
    # In[35]:

    browser = Browser('chrome', headless=False)
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(5)


    # In[36]:


    html = browser.html
    soup = BeautifulSoup(html, 'lxml')
    print(soup.prettify())


    # In[37]:


    # soup.body.prettify()


    # In[38]:


    # Extract news title text
    title = soup.find('div', class_='bottom_gradient').text
    print(title)


    # In[39]:


    # Extract paragraph text
    paragraph = soup.find('div', class_='rollover_description_inner').text
    print(paragraph)


    # ### JPL Mars Space Images - Featured Image

    # In[7]:


    # Visit the url for JPL's Featured Space Image here.
    # Use splinter to navigate the site and find the image url for 
    # the current Featured Mars Image and assign the url string to a variable called featured_image_url.
    # Make sure to find the image url to the full size .jpg image.
    # Make sure to save a complete url string for this image.

    # # Example:
    # featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'


    # In[11]:

      
    from splinter import Browser
    #img_url = 'https://www.jpl.nasa.gov/spaceimages/'
    
    #executable_path = {'executable_path': './chromedriver'}
    #browser = Browser('chrome', **executable_path)
    #browser.visit(img_url)
    
    
    browser = Browser('chrome', headless=False)
    img_url = 'https://www.jpl.nasa.gov/spaceimages/'
    browser.visit(img_url)
    time.sleep(5)

    # In[12]:


    browser.click_link_by_id('full_image')


    # In[13]:

    time.sleep(5)
    browser.find_link_by_partial_text('more info').click()


    # In[14]:

    #time.sleep(5)
    #browser.find_link_by_partial_text('.jpg').click()


    # In[15]:

    time.sleep(5)
    featured_image_url = browser.find_by_tag('img')[6]['src']
    featured_image_url


    # ### Mars Weather

    # In[16]:


    # Visit the Mars Weather twitter account here 
    # and scrape the latest Mars weather tweet from the page. 
    # Save the tweet text for the weather report 
    # as a variable called mars_weather.

    # Example:
    # mars_weather = \
    # 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa, daylight 06:09-17:55'


    # In[17]:

    from splinter import Browser
    browser = Browser('chrome', headless=False)
    tw_acct_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(tw_acct_url)
    time.sleep(5)


    # In[18]:


    html = browser.html
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify())


    # In[19]:


    container = soup.find('div', class_='js-tweet-text-container')
    container


    # In[20]:


    mars_weather = container.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    mars_weather


    # ### Mars Facts

    # In[21]:


    # Visit the Mars Facts webpage here and use Pandas 
    # to scrape the table containing facts about the planet 
    # including Diameter, Mass, etc.
    # Use Pandas to convert the data to a HTML table string.


    # In[22]:


    marsfacts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(marsfacts_url)
    tables


    # In[23]:


    df = tables[0]
    df


    # In[24]:


    df = df.rename(columns = {0:'Measurement',1:'Value'})
    df = df.set_index('Measurement')
    df


    # In[25]:


    # convert table to html string
    html_table = df.to_html()
    html_table


    # In[26]:


    # strip unwanted newlines to clean up the table.
    html_table = html_table.replace('\n', '')
    html_table


    # ### Mars Hemisperes

    # In[27]:


    # Visit the USGS Astrogeology site here to obtain 
    # high resolution images for each of Mar's hemispheres.
    # You will need to click each of the links to the hemispheres 
    # in order to find the image url to the full resolution image.
    # Save both the image url string for the full resolution hemipshere image, 
    # and the Hemisphere title containing the hemisphere name. 

    # Use a Python dictionary to store the data using the keys img_url and title.
    # Append the dictionary with the image url string and the hemisphere title to a list. 
    # This list will contain one dictionary for each hemisphere.

    # # Example:
    # hemisphere_image_urls = [
    #     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    #     {"title": "Cerberus Hemisphere", "img_url": "..."},
    #     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    #     {"title": "Syrtis Major Hemisphere", "img_url": "..."},
    # ]


    # In[28]:

    from splinter import Browser
    browser = Browser('chrome', headless=False)
    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(usgs_url)
    time.sleep(5)


    # In[29]:


    browser.find_by_css('h3')[0].click()
    img1_url = browser.find_by_tag('a')[41]['href']
    print(img1_url)

    img1_title = browser.find_by_css('h2')[0].text
    img1_title = img1_title.replace(' Enhanced', '')
    print(img1_title)


    # In[30]:


    browser.back()
    browser.find_by_css('h3')[1].click()
    img2_url = browser.find_by_tag('a')[41]['href']
    print(img2_url)

    img2_title = browser.find_by_css('h2')[0].text
    img2_title = img2_title.replace(' Enhanced', '')
    print(img2_title)


    # In[31]:


    browser.back()
    browser.find_by_css('h3')[2].click()
    img3_url = browser.find_by_tag('a')[41]['href']
    print(img3_url)

    img3_title = browser.find_by_css('h2')[0].text
    img3_title = img3_title.replace(' Enhanced', '')
    print(img3_title)


    # In[32]:


    browser.back()
    browser.find_by_css('h3')[3].click()
    img4_url = browser.find_by_tag('a')[41]['href']
    print(img4_url)

    img4_title = browser.find_by_css('h2')[0].text
    img4_title = img4_title.replace(' Enhanced', '')
    print(img4_title)


    # In[33]:


    # Use a Python dictionary to store the data using the keys img_url and title.
    hemisphere_img_dict = [
        {"title": img1_title, "img_url": img1_url},
        {"title": img2_title, "img_url": img2_url},
        {"title": img3_title, "img_url": img3_url},
        {"title": img4_title, "img_url": img4_url},
    ]

    

    data_outputs = {'title': title,
        'paragraph': paragraph,
        'featured_image_url': featured_image_url,
        'mars_weather': mars_weather,
        'html_table': html_table,
        'hemisphere_img_dict': hemisphere_img_dict}

    mars_data.insert(data_outputs)
    return data_outputs
    # ##### End of Script
