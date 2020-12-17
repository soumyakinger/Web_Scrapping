from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/Users/tusharkinger/.wdm/drivers/chromedriver/mac64/87.0.4280.88/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_data = {}
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    news_title = soup.find("div", class_="image_and_description_container").find("div",class_="content_title").get_text()
    news_desc = soup.find("div", class_="image_and_description_container").find("div", class_="rollover_description_inner").get_text()

    mars_data["news_title"] = news_title
    mars_data["news_desc"] = news_desc

    url = 'https://www.jpl.nasa.gov/spaceimages/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image = soup.find("div", class_="carousel_items")
    image_url = featured_image.article['style']
    partial_url = image_url.split(':')[1].split('spaceimages/')[1].split("\''")
    featured_image_url = url+partial_url[0]

    mars_data["featured_image_url"] = featured_image_url


    comparison_column = []
    mars = []
    earth = []
    currentrow = []
    comparison_table = []
    headerrow = []

    #Set the url to space-facts.com/mars webpage
    url = 'https://space-facts.com/mars/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    #Use beautiful soup to parse the webpage
    tableheader = soup.find("table", id = "tablepress-comp-mars").find("thead").find("tr")
    tablerows = soup.find("table", id="tablepress-comp-mars").find("tbody").find_all("tr")
    for row in tablerows:
        rowdata = row.find_all("td")
        for td in rowdata:
            currentrow.append(td.text.strip())
        comparison_table.append(currentrow)
        currentrow = []
    
    for i in range(len(comparison_table)):
        comparison_column.append(comparison_table[i][0])
        mars.append(comparison_table[i][1])
        earth.append(comparison_table[i][2])
    


    firstcolumn = tableheader.find("th", class_="column-1").find("strong").text.strip()
    secondcolumn = tableheader.find("th", class_="column-2").find("span").text.strip()
    
 
    #print(firstcolumn,secondcolumn,thirdcolumn)
    #print(headerrow)
    data = {firstcolumn:comparison_column,secondcolumn:mars}
    #Save the dictioary as a pandas dataframe
    #table_df = pd.DataFrame.from_dict(data)
    mars_data["mars_dim_colhead1"] = firstcolumn
    mars_data["mars_dim_colhead2"] = secondcolumn
    mars_data["mars_dim_col1"] = comparison_column
    mars_data["mars_dim_col2"] = mars

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    partial_url = url.split("/search")[0]
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    hemisphere_image_urls = []
    #Use beautiful soup to parse image links and titles for all the hemispheres
    hemisphere_list = soup.find_all("div", class_="item")
    for item in hemisphere_list:
    
        hemisphere_details = {}
        image_link = item.find("a", class_="itemLink product-item")
        image_link_url = image_link.find("img")["src"]
        image_title = item.find("div",class_="description").find("a").find("h3").get_text()
        hemisphere_details["image_link_url"] = partial_url+image_link_url
        hemisphere_details["title"] = image_title
        hemisphere_image_urls.append(hemisphere_details)

    mars_data["hemisphere_image_urls"] = hemisphere_image_urls
    
    return mars_data




