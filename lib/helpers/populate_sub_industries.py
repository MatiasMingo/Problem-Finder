import json
import requests
from bs4 import BeautifulSoup
from time import sleep

def load_industries_dict():
    with open("Data/industries.json", 'r', encoding="utf-8") as industries_file:
        industries_dict = json.load(industries_file)
    return industries_dict  

def write_industries_dict(industries_dict):
    with open("Data/industries.json", 'w', encoding="utf-8") as industries_file:
        json.dump(industries_dict, industries_file)

def convert_list_subindustries():
    industries_dict = load_industries_dict()
    industries_list = list(industries_dict.keys())
    with open("Data/subindustries.txt", 'r', encoding="utf-8") as industries_file:
        current_industry = ""
        for line in industries_file:
            clean_line = line.strip("\n").strip(" ").split("in the US",1)[0].replace("in the US", '').strip()
            if clean_line in industries_list:
                current_industry = clean_line
                industries_dict[current_industry] = []
                continue
            else:
                industries_dict[current_industry].append(clean_line)
    write_industries_dict(industries_dict)
    return industries_dict  

def clean_subindustry_name(subindustry):
    clean_str = subindustry.strip("in the US")
    return clean_str

def scrape_sub_industries():
    industries_dict = load_industries_dict()
    url = "https://www.ibisworld.com/united-states/list-of-industries/"
    response = requests.get(url)
    sleep(2)
    soup = BeautifulSoup(response.content, "html.parser")
    subindustries_columns = soup.find_all("div")
    for subindustry_column in subindustries_columns:
        print(subindustry_column.text)


convert_list_subindustries()