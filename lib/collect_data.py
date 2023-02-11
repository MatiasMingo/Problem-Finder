import json
from .APIs import twitter_interaction
from time import sleep
from .Scrapping import google_news

def get_industries_dict():
    with open("Data/industries.json", 'r', encoding="utf-8") as industries_file:
        industries_dict = json.load(industries_file)
    return industries_dict  

def write_subindustry_tweets_dict(industries_dict):
    with open("Data/industry_tweets.json", 'w', encoding="utf-8") as industries_file:
        json.dump(industries_dict, industries_file)


def get_viewed_tweets_dict():
    with open("Data/viewed_tweets.json", 'r', encoding="utf-8") as viewed_tweets_file:
        viewed_tweets_dict = json.load(viewed_tweets_file)
    return viewed_tweets_dict  

def write_viewed_tweets_dict(viewed_tweets_dict):
    with open("Data/viewed_tweets.json", 'w', encoding="utf-8") as viewed_tweets_file:
        json.dump(viewed_tweets_dict, viewed_tweets_file)

def search_tweets(industries_dict):
    dict_subindustry_tweets = {}
    viewed_tweets_dict = get_viewed_tweets_dict()
    for industry, subindustries_list in industries_dict.items():
        for subindustry in subindustries_list:
            print(subindustry)
            try:
                subindustry = subindustry.lower()
                key_words = [subindustry]
                tweets = twitter_interaction.search_tweets(key_words)
                tweets_list = []
                for tweet in tweets:
                    if 'RT' in tweet._json['full_text'].split(" "):
                        continue
                    if tweet._json['id_str'] not in viewed_tweets_dict['ids']:
                        tweets_list.append(tweet._json['full_text'])
                        viewed_tweets_dict['ids'].append(tweet._json['id_str'])
                        write_viewed_tweets_dict(viewed_tweets_dict)
                dict_subindustry_tweets[subindustry] = tweets_list
                write_subindustry_tweets_dict(dict_subindustry_tweets)  
            except Exception as e:
                print(e)
                print(dict_subindustry_tweets)
                write_subindustry_tweets_dict(dict_subindustry_tweets)  
                sleep(900)
    write_subindustry_tweets_dict(dict_subindustry_tweets)