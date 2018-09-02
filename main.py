import requests
from bs4 import BeautifulSoup
import os.path
import hashlib
import json

url = "https://www.indeed.co.uk/jobs"
search_term = "q=python"
location = "&l=London"
page = 0
increment = 10
cache_folder = './cache/'

url = url + search_term + location + '&start=' + str(page)

# cache
cache_filename = hashlib.md5(url.encode('utf-8')).hexdigest()
file_exists = os.path.isfile(cache_filename) 
if not file_exists:
    response = requests.get(url)
    with open(cache_folder + cache_filename, 'a') as cf:
        cf.write(response.text)

with open(cache_folder + cache_filename, 'r') as cf:
    response = cf.read()

soup = BeautifulSoup(response, 'html.parser')

results = soup.select('div.result')



# "https://www.indeed.co.uk/company/Baaltek/jobs/Python-Developer-7edaca00286cff06?fccid=c2be16111c46764a&vjs=3"


for k, result in enumerate(results):
    anchors = result.select('a[href]')
    print(anchors)
    




