import requests
import os.path
import hashlib
from bs4 import BeautifulSoup
from scrappers.scrapper import Scrapper
import urllib
import datetime

class Tiobe(Scrapper):

    def __init__(self, log):
        self.log = log


    def run(self):
        self.log.info("Running " + __name__)
        url = "https://www.tiobe.com/tiobe-index/"
        
        # cache_filename = hashlib.md5(url.encode('utf-8')).hexdigest() + ".html"
        cache_filename = 'tiobe-' + str(datetime.date.today()) + '.html'
        response = self.get_from_cache(cache_filename, url)
        
        soup = BeautifulSoup(response, 'html.parser')
        results = soup.select('table.table-striped')
        
        self.process_results(results)


    def process_results(self, results):
        top_languages = []
        for k, result in enumerate(results):
            rows = result.select('tr')
            
            if (k > 1):
                break

            # remove the header
            header = rows.pop(0)

            print('table:', k)
            
            for j, row in enumerate(rows):
                

                info = row.find_all('td')

                # First part of the table is composed of more than 3 elements
                # second part has only 3
                # and then theres other tables we dont care about
                if (len(info) > 3):
                    language = {
                        'position': info[0].text,
                        'name': info[3].text,
                        'share': info[4].text,
                        'monthly_change': info[5].text,
                    }
                else:    
                    language = {
                        'position': info[0].text,
                        'name': info[1].text,
                        'share': info[2].text,
                    }
                
                top_languages.append(language)
            
        self.persist(top_languages)
    
    def persist(self, top_languages):
        pass
            


    def get_from_cache(self, cache_filename, url):
        cache_folder = './src/cache/'
        file_exists = os.path.isfile(cache_filename) 
        if not file_exists:
            response = requests.get(url)
            with open(cache_folder + cache_filename, 'a') as cf:
                cf.write(response.text)
        with open(cache_folder + cache_filename, 'r') as cf:
            response = cf.read()
        
        return response

