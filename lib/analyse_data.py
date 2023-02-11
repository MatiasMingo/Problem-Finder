import json
from .helpers import sentiment_analysis
from time import sleep

def get_industries_dict():
    with open("Data/industries.json", 'r', encoding="utf-8") as industries_file:
        industries_dict = json.load(industries_file)
    return industries_dict  

def get_industry_tweets_dict():
    with open("Data/industry_tweets.json", 'r', encoding="utf-8") as industries_file:
        industries_dict = json.load(industries_file)
    return industries_dict  

def get_industry_sentiment_dict():
    with open("Data/industry_sentiment.json", 'r', encoding="utf-8") as industries_file:
        industries_dict = json.load(industries_file)
    return industries_dict

def write_subindustry_sentiment_dict(industries_dict):
    with open("Data/industry_sentiment.json", 'w', encoding="utf-8") as industries_file:
        json.dump(industries_dict, industries_file)

def get_viewed_tweets():
    with open("Data/viewed_tweets.json", 'r', encoding="utf-8") as viewed_tweets_file:
        viewed_tweets_dict = json.load(viewed_tweets_file)
    return viewed_tweets_dict

def analyse_data():
    industries_dict = get_industries_dict()
    industry_tweets_dict =  get_industry_tweets_dict()
    industry_sentiment_dict = get_industry_sentiment_dict()
    for industry, subindustry_list in industries_dict.items():
        if industry not in industry_sentiment_dict.keys():
            industry_sentiment_dict[industry] = {}
        for subindustry in subindustry_list:
            print(subindustry)
            subindustry = subindustry.lower()
            if subindustry not in industry_sentiment_dict[industry].keys():
                industry_sentiment_dict[industry][subindustry] = {"positive": 0, "negative": 0}
            tweets =  industry_tweets_dict[subindustry]
            for tweet in tweets:
                try:
                    sentiment = sentiment_analysis.analyse_sentiment(tweet)[0]
                    if round(float(sentiment['score']),3) > 0.7:
                        industry_sentiment_dict[industry][subindustry]["positive"] += 1
                    elif round(float(sentiment['score']),3) < 0.3:
                        industry_sentiment_dict[industry][subindustry]["negative"] += 1
                    write_subindustry_sentiment_dict(industry_sentiment_dict)
                except Exception as e:
                    print(e)
                    write_subindustry_sentiment_dict(industry_sentiment_dict)
                    sleep(60)
    print(industry_sentiment_dict)
    write_subindustry_sentiment_dict(industry_sentiment_dict)