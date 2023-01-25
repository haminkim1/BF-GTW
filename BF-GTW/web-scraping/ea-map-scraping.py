# Scrape images from ea.com
from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
from random import randrange



def main():
    # link = getBFVLinks()
    bfvLink = "https://www.ea.com/games/battlefield/battlefield-5/about/maps"
    bf1Link = "https://www.ea.com/games/battlefield/battlefield-1/maps"
    bf2042Link = "https://www.ea.com/games/battlefield/battlefield-2042/game-overview/maps"
    getBFVImage(bfvLink)
    getBF1Image(bf1Link)
    getBF2042Image(bf2042Link)
    # getBF2042Image()


def soupURL(link):
    page_url = link
    uClient = uReq(page_url)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    return page_soup


def getBFVImage(link):
    page_soup = soupURL(link)
    images = page_soup.findAll("img", {"width": "100%"})
    randomNumber = randrange(len(images))
    image = images[randomNumber]["src"]

    print(image)
    return image


def getBF1Image(link):
    page_soup = soupURL(link)
    images = page_soup.findAll("ea-tile", {"slot": "tile"}, {"style": "--ea-animation-index:5"})
    randomNumber = randrange(len(images))
    image = images[randomNumber]["media"]

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


# def getBF4Image(link):


if __name__ == "__main__":
    main()



