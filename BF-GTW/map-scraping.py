from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client

# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
# page_url = "https://battlefield.fandom.com/wiki/Template:Maps/BF5"

# uClient = uReq(page_url)

# page_soup = soup(uClient.read(), "html.parser")
# uClient.close()

def main():
    links = getBFVLinks()
    getBFVImages(links)


def soupURL(link):
    page_url = link

    uClient = uReq(page_url)

    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    return page_soup


def getBFVLinks():
    page_soup = soupURL("https://battlefield.fandom.com/wiki/Template:Maps/BF5")

    # Try the BF wiki page first (https://battlefield.fandom.com/wiki/Battlefield_V)

    # Find the HTML content of "Multiplayer Levels of Battlefield V table where it shows the map names"
    td = page_soup.find("table", {"class": "nowraplinks"}).tbody.findAll("td", {"class": "navbox-list"})

    # Find the text containing the href of the map within HTML and append on a list
    a_tag = []
    links = []

    for i in range(len(td)):
        a_tag += td[i].select("a")

    for i in a_tag:
        links.append(i["href"])
    # print(links)
    return links


# For each name, go to battlefield.fandom.com/wiki/{map_name}
def getBFVImages(links):

    images = []
    test = links[0]
    for link in links:
        page_soup = soupURL("https://battlefield.fandom.com{}".format(link))

        # Find the HTML tag of the image of the map. 

        # image from a tag gives a much larger image. 
        # figure = page_soup.find("figure", {"class": "pi-item"}).find("a")
        
        # Copy the link of each image and paste it into a list. 
        # images.append(figure["href"])
    # print(images)


        # This part of the code scrapes in link from the img tag which is much smaller. 
        # Determine which link is best for my project. 
        #  Copy the link of each image and paste it into a list. 
        figure = page_soup.find("figure", {"class": "pi-item"}).a.find("img")
        images.append(figure["src"])
    print(images)





if __name__ == "__main__":
    main()



