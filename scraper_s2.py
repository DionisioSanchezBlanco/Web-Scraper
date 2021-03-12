# Web scrapper
# To get Title and description of the some film
import requests
from bs4 import BeautifulSoup

film = {}


class Scrapper:
    def __init__(self, url):
        self.url = url

    def check_url(self):
        if 'title' not in self.url:
            print("Invalid movie page!")
        elif requests.get(self.url):
            scr.get_info()
        else:
            print("Invalid movie page!")

    def get_info(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        h1 = soup.find('div', {'class': 'originalTitle'}).text
        p = soup.find('div', {'class': 'summary_text'}).text
        film["title"] = h1
        film["description"] = p.strip()
        print(film)


scr = Scrapper(input("Input the URL:\n"))
scr.check_url()
