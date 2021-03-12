# Web scrapper
# Check the url inputed by user, if status code is 200:
# check the dictionary for 'content' key and display the data

import requests


class Scrapper:
    def __init__(self, url):
        self.url = url

    def check_url(self):
        if requests.get(self.url):
            r = requests.get(self.url)
            data = r.json()
            if 'content' in data.keys():
                print(data['content'])
            else:
                print("Invalid quote resource")
        else:
            print("Invalid quote resource")


scr = Scrapper(input("Input the URL:\n"))
scr.check_url()
