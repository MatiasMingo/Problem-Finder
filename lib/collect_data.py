import json
from time import sleep
from .Scrapping import google_news



def get_industries_dict(json_path):
    with open(json_path, 'r', encoding="utf-8") as industries_file:
        industries_dict = json.load(industries_file)
    return industries_dict  

def find_industry_processes(industries_dict):
    url_dicts = {}
    for key, industries in industries_dict.items():
        for industry in industries:
            print(f'{industry} \n')
            url_news, url_search = google_news.get_industry_news(industry)
            url_dicts[industry] = [url_news, url_search]
    write_industry_processes_json(url_dicts)
    
def write_industry_processes_json(urls_dict):
    with open("Data/Results/research_links.json", 'w', encoding="utf-8") as industries_file:
        industries_dict = json.dump(urls_dict, industries_file)
    return industries_dict