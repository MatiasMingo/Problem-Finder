import requests
from bs4 import BeautifulSoup
from time import sleep

def scrape_news(keywords):
    # create the search query
    query = "+".join(keywords)
    url = f"https://news.google.com/search?q={query}&hl=en-US&gl=US&ceid=US:en"

    # request the website
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    # extract the relevant information
    articles = []
    for article in soup.select('article'):
        title = article.select_one('a[class*="DY5T1d"]').get_text()
        timestamp = article.select_one('time').get_text()
        link = article.select_one('a[class*="DY5T1d"]').get('href')
        content = get_article_content(link[1:-1])
        articles.append({'title': title, 'content': content, 'timestamp': timestamp})
    return articles

def get_article_content(link):
    link = "https://news.google.com{}".format(link)
    res = requests.get(link)
    sleep(5)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = soup.select_one('div[class*="xBbh9"]').get_text()
    return content

def get_industries_news(industries_dict):
    keywords = ["machine learning", "artificial intelligence"]
    scraped_articles = scrape_news(keywords)
    print(scraped_articles)
