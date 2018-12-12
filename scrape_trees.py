from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

tree_list = ['london plane tree']

 url = "http://leafsnap.com/species/
 browser.visit(url)

 html = browser.html
 soup = bs(html, "html.parser")

ne_species = soup.find('div', id='species-1')

    # Get the min avg temp
species = ne_species.find_all('td')

for tree in species:
    leaf = species[0]
    name = species[3]
    print(name)




""" def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit visitcostarica.herokuapp.com
    url = "http://leafsnap.com/species/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the average temps
    ne_species = soup.find('div', id='species-1')

    # Get the min avg temp
    species = avg_temps.find_all('td')

    for tree in species:
        leaf = species[0]
        name = species[3]

    # BONUS: Find the src for the sloth image
    relative_image_path = soup.find_all('img')[2]["src"]
    sloth_img = url + relative_image_path

    # Store data in a dictionary
    costa_data = {
        "sloth_img": sloth_img,
        "min_temp": min_temp,
        "max_temp": max_temp
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return costa_data
 """