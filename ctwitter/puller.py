import os
from twitter import *
import json


class Puller():

    log = None
    token = None
    token_secret = None
    consumer_key = None
    consumer_secret = None

    def __init__(self, log):
        self.log = log
        self.token = os.getenv('TWITTER_TOKEN')
        self.token_secret = os.getenv('TWITTER_TOKEN_SECRET')
        self.consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        self.consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')


    def run(self):
        t = Twitter(auth = OAuth(self.token, self.token_secret, self.consumer_key, self.consumer_secret))

        # Get your "home" timeline
        # home = t.statuses.home_timeline(count = 5)

        # Get a particular friend's timeline
        # rtimeline = t.statuses.user_timeline(screen_name = "roycocup")

        # to pass in GET/POST parameters, such as `count`
        # t.statuses.home_timeline(count = 5)

        # x = t.statuses.home_timeline(count = 5)
        # print(x[0]['user']['screen_name'])

        # to pass in the GET/POST parameter `id` you need to use `_id`
        # t.statuses.oembed(_id=1234567890)
