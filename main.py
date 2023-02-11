from lib import collect_data, analyse_data, output_data
from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess as cmd


def job():
    industries_dict = collect_data.get_industries_dict()
    collect_data.search_tweets(industries_dict)
    analyse_data.analyse_data()
    #output_data()

if __name__ == '__main__':
	while True:
		job()