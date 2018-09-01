import requests
from bs4 import BeautifulSoup

url = "https://www.indeed.co.uk/jobs?q=python&l=London"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# results = soup.find_all('div', {"class": "result"})
results = soup.select('div.result')


# for result in results:
#     result.children
link = "https://www.indeed.co.uk/company/Baaltek/jobs/Python-Developer-7edaca00286cff06?fccid=c2be16111c46764a&vjs=3"
links = results[0].find_all('a')
print(links)



