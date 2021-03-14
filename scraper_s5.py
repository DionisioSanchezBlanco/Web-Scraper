# Web scrapper
# Final Stage
# Save in txt files articles from https://www.nature.com/nature/articles
# User will input number of pages to check and the category
# One folder for each page will store the articles.

import requests
from bs4 import BeautifulSoup
import string
import os

list_articles = []


class Scrapper:
    def __init__(self, url, pages, category):
        self.url = url
        self.pages = pages
        self.category = category
        self.list_articles = []
        self.list_directories = []

    '''def check_url(self):
        r = requests.get(self.url)
        if r:
            scr.get_info()
        else:
            print(f"The URL returned {r.status_code}!")'''

    def get_info(self):
        i = 1

        while i in range(1, self.pages + 1):
            current_page = f"searchType=journalSearch&sort=PubDate&page={i}"
            r = requests.get(self.url, params=current_page)

            soup = BeautifulSoup(r.text, 'html.parser')
            articles = soup.find_all('article', attrs={'itemtype': 'http://schema.org/ScholarlyArticle'})

            for items in articles:
                news = items.find('span', attrs={'class': 'c-meta__type'}).text
                if news == self.category:
                    links = items.find('a', href=True, attrs={'data-track-action': 'view article'})
                    self.list_articles.append(f"https://www.nature.com{links['href']}")

            j = i - 1
            #print(list_articles)
            scr.save_articles(self.list_directories[j])
            self.list_articles.clear()

            i += 1

    def save_articles(self, folder):
        for articles in self.list_articles:
            r = requests.get(articles)
            soup = BeautifulSoup(r.text, 'html.parser')
            title = soup.find('h1', attrs={'class': 'article-item__title'}).text
            title = title.replace(':', '')
            title = title.replace("'", '')
            title = title.replace(",", "")
            title = title.replace("-", "")
            title = title.replace(' ', '_') + '.txt'
            try:
                body = soup.find('div', attrs={'class': 'article__body'}).text
            except:
                body = soup.find('div', attrs={'class': 'article-item__body'}).text

            #print(body)
            with open(f'{folder}/{title}', 'w', encoding='utf8') as file:
                file.write(body)

    def create_directory(self):
        i = 1
        while i in range(1, self.pages + 1):
            os.mkdir(f'Page_{i}')
            self.list_directories.append(f'Page_{i}')
            i += 1


pages = int(input())
category = input()
scr = Scrapper("https://www.nature.com/nature/articles", pages, category)
scr.create_directory()
scr.get_info()
print('Saved all articles')
