# Web scrapper
# Get articles from https://www.nature.com/nature/articles
# 1. Get the links only for articles in 'News' category.
# 2. Get the title and content of each article.
# Save the information on [article_name].txt file

import requests
from bs4 import BeautifulSoup
import string

list_articles = []


class Scrapper:
    def __init__(self, url):
        self.url = url
        self.list_articles = []

    def check_url(self):
        r = requests.get(self.url)
        if r:
            scr.get_info()
        else:
            print(f"The URL returned {r.status_code}!")

    def get_info(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        articles = soup.find_all('article', attrs={'itemtype': 'http://schema.org/ScholarlyArticle'})

        for items in articles:
            news = items.find('span', attrs={'class': 'c-meta__type'}).text
            if news == 'News':
                links = items.find('a', href=True, attrs={'data-track-action': 'view article'})
                self.list_articles.append(f"https://www.nature.com{links['href']}")

    def save_articles(self):
        for articles in self.list_articles:
            r = requests.get(articles)
            soup = BeautifulSoup(r.text, 'html.parser')
            title = soup.find('title').text
            title = title.replace(':', '')
            title = title.replace("'", '')
            title = title.replace(' ', '_') + '.txt'
            body = soup.find('div', attrs={'class': 'article__body'}).text
            print(body)
            with open(title, 'w', encoding='utf8') as file:
                file.write(body)


scr = Scrapper("https://www.nature.com/nature/articles")
scr.check_url()
scr.save_articles()
