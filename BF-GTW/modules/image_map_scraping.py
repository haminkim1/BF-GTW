# Scrape images from ea.com
from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq, Request  # Web client
import ssl
import certifi

from random import randrange




def scrapeImages():
    bf4Link = "https://wallpapercave.com/battlefield-4-wallpapers"
    bf1Link = "https://www.ea.com/games/battlefield/battlefield-1/maps"
    bfvLink = "https://www.ea.com/games/battlefield/battlefield-5/about/maps"
    bf2042Link = "https://www.ea.com/games/battlefield/battlefield-2042/game-overview/maps"

    images = {}
    images["bf4"] = getBF4Image(bf4Link)
    images["bf1"] = getBF1Image(bf1Link)
    images["bfv"] = getBFVImage(bfvLink)
    images["bf2042"] = getBF2042Image(bf2042Link)

    return images


# Webpage that is being scraped blocks/forbids users when trying to soup without Mozilla/5.0 headers. 
# Therefore, the BF4 page is scraped slightly differently than other games. 
def soupBF4URL(link):
    req = Request(
        url=link, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    webpage = uReq(req).read()
    page_soup = soup(webpage, "html.parser")
    return page_soup


def soupURL(page_url):
    context = ssl.create_default_context(cafile=certifi.where())
    uClient = uReq(page_url, context=context)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()
    return page_soup


def getBF4Image(link):
    page_soup = soupBF4URL(link)
    div = page_soup.find("div", {"id": "albumwp"})
    images = div.findAll("img", {"class": "wimg"})

    randomNumber = randrange(len(images))
    image = "https://wallpapercave.com" + images[randomNumber]["src"]
    # print(image)
    return image


def getBF1Image(link):
    page_soup = soupURL(link)
    images = page_soup.findAll("ea-tile", {"slot": "tile"}, {"style": "--ea-animation-index:5"})
    randomNumber = randrange(len(images))
    image = images[randomNumber]["media"]

    # print(image)
    return image


def getBFVImage(link):
    page_soup = soupURL(link)
    images = page_soup.findAll("img", {"width": "100%"})
    randomNumber = randrange(len(images))
    image = images[randomNumber]["src"]

    # print(image)
    return image


def getBF2042Image(link):
    page_soup = soupURL(link)
    ironPages = page_soup.find("iron-pages")
    images = ironPages.findAll("img")
    randomNumber = randrange(len(images))
    image = images[randomNumber]["src"]

    # print(image)
    return(image)




