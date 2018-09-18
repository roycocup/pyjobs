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

        results = soup.select('table.table-striped')
        
        results_filename = self.cache_results(cache_filename)
        self.process_results(results, results_filename)


    def process_results(self, results, results_filename):
        for k, result in enumerate(results):
            rows = result.select('tr')
            
            # remove the header
            header = rows.pop(0)
            for row in rows:
                info = row.find_all('td')
            
            

    def cache_results(self, cache_filename):
        results_filename = './cache/' + cache_filename
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

