import requests
from bs4 import BeautifulSoup

class Web_Scraper():
    def get_response(url):
        return requests.get(url=url)

    def get_links(url):
        soup = BeautifulSoup(Web_Scraper.get_response(url).content, 'html.parser')

        allLinks = soup.find(id="bodyContent").find_all("a")
        wiki_links = []

        for link in allLinks:
            if Web_Scraper.is_wiki(link) and not Web_Scraper.is_image(link):
                wiki_links.append(link.get('href')[6:])

        return wiki_links
            
    def is_wiki(link):
        return link.get('href') is not None and link.get('href').find("/wiki/")!=-1

    def is_image(link):
        img_class = link.get('class')
        if img_class is not None:
            return any([i == 'image' or i == 'thumbimage'for i in img_class])
        return False

