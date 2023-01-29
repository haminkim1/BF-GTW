# Scrape images from ea.com
from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq, Request  # Web client

from random import randrange




def scrapeImages():
    # link = getBFVLinks()
    bf4Link = "https://wallpapercave.com/battlefield-4-wallpapers"
    bf1Link = "https://www.ea.com/games/battlefield/battlefield-1/maps"
    bfvLink = "https://www.ea.com/games/battlefield/battlefield-5/about/maps"
    bf2042Link = "https://www.ea.com/games/battlefield/battlefield-2042/game-overview/maps"

    images = {}
    images["bf4"] = getBF1Image(bf4Link)
    images["bf1"] = getBF1Image(bf1Link)
    images["bfv"] = getBFVImage(bfvLink)
    images["bf2042"] = getBF2042Image(bf2042Link)
    # getBF2042Image()
    return images


def getBF4Page(link):
    req = Request(
        url=link, 
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    webpage = uReq(req).read()
    page_soup = soup(webpage, "html.parser")
    return page_soup


def soupURL(link):
    page_url = link
    uClient = uReq(page_url)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()
    return page_soup


def getBF4Image(link):
    page_soup = getBF4Page(link)
    div = page_soup.find("div", {"id": "albumwp"})
    images = div.findAll("img", {"class": "wimg"})

    randomNumber = randrange(len(images))
    image = "https://wallpapercave.com" + images[randomNumber]["src"]
    print(image)


def getBF1Image(link):
    page_soup = soupURL(link)
    images = page_soup.findAll("ea-tile", {"slot": "tile"}, {"style": "--ea-animation-index:5"})
    randomNumber = randrange(len(images))
    image = images[randomNumber]["media"]

    print(image)
    return image


def getBFVImage(link):
    page_soup = soupURL(link)
    images = page_soup.findAll("img", {"width": "100%"})
    randomNumber = randrange(len(images))
    image = images[randomNumber]["src"]

    print(image)
    return image


def getBF2042Image(link):
    page_soup = soupURL(link)
    ironPages = page_soup.find("iron-pages")
    images = ironPages.findAll("img")
    randomNumber = randrange(len(images))
    image = images[randomNumber]["src"]

    print(image)
    return(image)




