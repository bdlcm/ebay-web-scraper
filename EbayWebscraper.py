from bs4 import BeautifulSoup
import requests

name_list = ["Ramen", "Monster Hunter World", "Adhesive page markers", "Calculator", "arduino", "gtx 1070",
             "bluetooth headphones", "coffee machine", "sweet tea", "Python textbook"]

def make_urls(names):
    # eBay url that can be modified to search for a specific item on eBay
    url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312.R1.TR11.TRC2.A0.H0.XIp.TRS1&_nkw="
    # List of urls created
    urls = []

    for name in names:
        # Adds the name of item being searched to the end of the eBay url and appends it to the urls list
        # In order for it to work the spaces need to be replaced with a +
        urls.append(url + name.replace(" ", "+"))

    # Returns the list of completed urls
    return urls

def ebay_scrape(urls):
    for url in urls:
        # Downloads the eBay page for processing
        res = requests.get(url)
        # Raises an exception error if there's an error downloading the website
        res.raise_for_status()
        # Creates a BeautifulSoup object for HTML parsing
        soup = BeautifulSoup(res.text, 'html.parser')
        # Scrapes the first listed item's name
        name = soup.find("h3", {"class": "s-item__title"}).get_text(separator=u" ")
        # Scrapes the first listed item's price
        price = soup.find("span", {"class": "s-item__price"}).get_text()

        # Prints the url, listed item name, and the price of the item
        print(url)
        print("Item Name: " + name)
        print("Price: " + price + "\n")

ebay_scrape(make_urls(name_list))
