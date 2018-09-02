import requests
from bs4 import BeautifulSoup
import os.path
import hashlib
import json
import re



def compose_url(url, search_term, location, page, increment):
    search_term = "q=" + search_term
    location = "&l=" + location 
    page = '&start=' + str(page)
    return url + "?" + search_term + location + page


def get_from_cache(filename):
    file_exists = os.path.isfile(cache_filename) 
    if not file_exists:
        response = requests.get(url)
        with open(cache_folder + cache_filename, 'a') as cf:
            cf.write(response.text)

    with open(cache_folder + cache_filename, 'r') as cf:
        response = cf.read()
    
    return response    


url = "https://www.indeed.co.uk/jobs"
page = 0
increment = 10
cache_folder = './cache/'

url = compose_url(url, "python", "london", page, increment)

# print("URl: " + url)

cache_filename = hashlib.md5(url.encode('utf-8')).hexdigest()
response = get_from_cache(cache_filename)

soup = BeautifulSoup(response, 'html.parser')

results = soup.select('div.result')


# reset file if existed
results_filename = 'results/' + cache_filename + ".txt"
with open(results_filename, 'w+') as f:
    f.close

uniq_anchors = list()
for k, result in enumerate(results):
    anchors = result.select('a[href]')
    for anchor in anchors:
        href = anchor.attrs['href']
        if str(href).endswith('&vjs=3'):
            # if result is unique
            if not any(href in s for s in uniq_anchors):
                uniq_anchors.append(href)
                with open(results_filename, 'a') as f:
                    f.write(href+"\n")

    




