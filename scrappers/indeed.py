import requests
import os.path
import hashlib
from bs4 import BeautifulSoup
from scrappers.scrapper import Scrapper

class Indeed(Scrapper):

    def __init__(self, log):
        self.log = log


    def run(self):
        self.log.info("Running " + __name__)
        url = "https://www.indeed.co.uk/jobs"
        page = 0
        increment = 10

        url = self.compose_url(url, "python", "london", page, increment)
        cache_filename = hashlib.md5(url.encode('utf-8')).hexdigest()
        response = self.get_from_cache(cache_filename, url)

        soup = BeautifulSoup(response, 'html.parser')

        results = soup.select('div.result')

        results_filename = self.save_results(cache_filename)

        self.process_results(results, results_filename)

    def process_results(self, results, results_filename):
        uniq_anchors = list()
        for k, result in enumerate(results):
            anchors = result.select('a[href]')
            self.process_anchors(anchors, results_filename, uniq_anchors)

    def save_results(self, cache_filename):
        results_filename = 'results/' + cache_filename
        with open(results_filename, 'w+') as f:
            f.close
        return results_filename

    def compose_url(self, url, search_term, location, page, increment):
        search_term = "q=" + search_term
        location = "&l=" + location 
        page = '&start=' + str(page)
        return url + "?" + search_term + location + page


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

    def process_anchors(self, anchors, results_filename, uniq_anchors):
        for anchor in anchors:
            href = anchor.attrs['href']
            if str(href).endswith('&vjs=3'):
                # if result is not unique, then just continue
                if any(href in s for s in uniq_anchors):
                    continue
                uniq_anchors.append(href)
                with open(results_filename, 'a') as f:
                    f.write(href + "\n")







