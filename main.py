from lib import collect_data
#from lib import analyse_data
from lib import output_data
from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess as cmd




"""def job():
    industries_dict = collect_data.get_industries_dict()
    collect_data.search_tweets(industries_dict)
    analyse_data.analyse_data()
    #output_data()"""


def indentify_industries(json_path):
    industries_dict = collect_data.get_industries_dict(json_path)
    return industries_dict

def find_industry_processes(industries_dict):
    collect_data.find_industry_processes(industries_dict)

"""
    Niche finder:
        1. Indentify indrustries
        2. Find processes within those industries
        3. Find pain points for those processes
"""

if __name__ == '__main__':
    industries_dict = indentify_industries("Data/Industries/extremely_interesting_industries.json")
    find_industry_processes(industries_dict)
    