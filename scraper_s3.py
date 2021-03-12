# Web scrapper
# To get current webpage code
# It displays status code if the page is not available

import requests

film = {}


class Scrapper:
    def __init__(self, url):
        self.url = url

    def check_url(self):
        r = requests.get(self.url)
        if r:
            scr.get_info()
        else:
            print(f"The URL returned {r.status_code}!")

    def get_info(self):
        r = requests.get(self.url)
        with open("source.html", "wb") as f:
            f.write(r.content)
        print("Content saved.")


scr = Scrapper(input("Input the URL:\n"))
scr.check_url()
