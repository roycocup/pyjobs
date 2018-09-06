import os
from twitter import *
import json
from datetime import date


class Consumer(object):

    log = None
    token = None
    token_secret = None
    consumer_key = None
    consumer_secret = None
    t = None

    def __init__(self, log):
        self.log = log
        self.token = os.getenv('TWITTER_TOKEN')
        self.token_secret = os.getenv('TWITTER_TOKEN_SECRET')
        self.consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        self.consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')

    def run(self):
        self.log.info("Running custom twitter")

        self.t = Twitter(auth = OAuth(self.token, self.token_secret, self.consumer_key, self.consumer_secret))

        response = self.get_from_cache("home-20180906")
        print(type(json.loads(response)))


    def get_from_cache(self, cache_filename):
        cache_folder = './cache/'
        file_exists = os.path.isfile(cache_filename) 
        if not file_exists:
            response = self.t.statuses.home_timeline(count=5)
            with open(cache_folder + cache_filename, 'a') as cf:
                cf.write(json.dumps(response))
        with open(cache_folder + cache_filename, 'r') as cf:
            response = cf.read()
        
        return response