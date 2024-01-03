import requests
from bs4 import BeautifulSoup
from time import sleep
import re

def scrape_news(keywords):
    # create the search query
    query = "+".join(keywords)
    url_news = f"https://news.google.com/search?q={query}&hl=en-US&gl=US&ceid=US:en"
    url_search = f"https://google.com/search?q={query}&hl=en-US&gl=US&ceid=US:en"
    print(f'{url_news}\n')
    print(f'{url_search}\n')
    return url_news, url_search

""" # request the website
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
return articles"""

def get_article_content(link):
    link = "https://news.google.com{}".format(link)
    res = requests.get(link)
    sleep(5)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = soup.select_one('div[class*="xBbh9"]').get_text()
    return content

def get_industry_news(industry):
    print()
    processed_name = industry.replace(" ", "%20").replace("&", "").replace("%20%20", "%20")
    keywords = [processed_name, "problems"]
    url_news, url_search = scrape_news(keywords)
    return url_news, url_search
    
