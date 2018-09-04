from twitter import *
from dotenv import load_dotenv
import os


class Puller():

    token = None
    token_secret = None
    consumer_key = None
    consumer_secret = None

    def __init__(self):
        self.token = os.getenv('TWITTER_TOKEN')
        self.token_secret = os.getenv('TWITTER_TOKEN_SECRET')
        self.consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        self.consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')


    def run(self): pass
        # t = Twitter(auth = OAuth(token, token_secret, consumer_key, consumer_secret))
        #
        # # Get your "home" timeline
        # t.statuses.home_timeline()
        #
        # # Get a particular friend's timeline
        # t.statuses.user_timeline(screen_name="billybob")
        #
        # # to pass in GET/POST parameters, such as `count`
        # t.statuses.home_timeline(count=5)
        #
        # # to pass in the GET/POST parameter `id` you need to use `_id`
        # t.statuses.oembed(_id=1234567890)
        #
        # # Update your status
        # t.statuses.update(
        #     status="Using @sixohsix's sweet Python Twitter Tools.")
        #
        # # Send a direct message
        # t.direct_messages.new(
        #     user="billybob",
        #     text="I think yer swell!")