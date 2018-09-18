import os
from twitter import *
import json
from datetime import date
import datetime
import re


class Consumer(object):

    log = None
    token = None
    token_secret = None
    consumer_key = None
    consumer_secret = None
    t = None
    search_str = ""
    num_items = 100

    def __init__(self, log, search_str):
        self.log = log
        self.token = os.getenv('TWITTER_TOKEN')
        self.token_secret = os.getenv('TWITTER_TOKEN_SECRET')
        self.consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        self.consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
        self.search_str = search_str

    def get_from_cache(self, cache_filename):
        cache_folder = './cache/'
        file_exists = os.path.isfile(cache_folder + cache_filename) 
        if not file_exists:
            response = self.t.search.tweets(q=self.search_str, count=self.num_items)
            with open(cache_folder + cache_filename, 'a') as cf:
                cf.write(json.dumps(response))
        with open(cache_folder + cache_filename, 'r') as cf:
            response = cf.read()
        
        return response

    def run(self):
        self.log.info("Running custom twitter")

        self.t = Twitter(auth = OAuth(self.token, self.token_secret, self.consumer_key, self.consumer_secret))

        # replace everything that is not a word with single dash 
        search_name = re.sub(r"[^\w\d]", '-', self.search_str)
        cache_filename = search_name + "-" + str(datetime.date.today())

        response = self.get_from_cache(cache_filename)
        responses = json.loads(response)
        
        for item in responses["statuses"]:
            print(item["text"])
        
