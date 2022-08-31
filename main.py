from _csv import writer

from bs4 import BeautifulSoup
import requests
import time
from datetime import date


def scrap_articles():
    url = "https://www.theverge.com/tech"
    page = requests.get(url)
    print(page)

    soup = BeautifulSoup(page.content, 'lxml')
    articles = soup.find_all(
        'div', class_="c-entry-box--compact c-entry-box--compact--article")
    with open(f'{date.today()}_theVerge.csv', 'w', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header = ['Headline', 'URL', 'Author', 'Published']
        thewriter.writerow(header)
        for index, article in enumerate(articles):
            id_number = index
            headline = article.find(
                'h2', class_="c-entry-box--compact__title").text
            url = article.find(
                'h2', class_="c-entry-box--compact__title").a['href']
            author = article.find('span', class_="c-byline__author-name").text
            date_published = article.find(
                'time', class_="c-byline__item").text.replace(" ", '')
            info = [headline, url, author, date_published]
            thewriter.writerow(info)


if __name__ == '__main__':
    while True:
        scrap_articles()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
