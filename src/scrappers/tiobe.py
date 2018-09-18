import requests
import os.path
import hashlib
from bs4 import BeautifulSoup
from scrappers.scrapper import Scrapper

class Tiobe(Scrapper):

    def __init__(self, log):
        self.log = log


    def run(self):
        self.log.info("Running " + __name__)
        url = "https://www.tiobe.com/tiobe-index/"
        
        cache_filename = hashlib.md5(url.encode('utf-8')).hexdigest()
        response = self.get_from_cache(cache_filename, url)

        soup = BeautifulSoup(response, 'html.parser')

        results = soup.select('div.result')

        results_filename = self.save_results(cache_filename)
        self.process_results(results, results_filename)


    def process_results(self, results, results_filename):
        for k, result in enumerate(results):
            anchors = result.select('table')
            

    def save_results(self, cache_filename):
        results_filename = 'results/' + cache_filename
        with open(results_filename, 'w+') as f:
            f.close
        return results_filename


    def get_from_cache(self, cache_filename, url):
        cache_folder = './cache/'
        file_exists = os.path.isfile(cache_filename) 
        if not file_exists:
            response = requests.get(url)
            with open(cache_folder + cache_filename, 'a') as cf:
                cf.write(response.text)
        with open(cache_folder + cache_filename, 'r') as cf:
            response = cf.read()
        
        return response

