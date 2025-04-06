import requests
from bs4 import BeautifulSoup

html_text = requests.get("https://www.techpowerup.com/ssd-specs/").text

soup = BeautifulSoup(html_text, 'lxml')
ssd = soup.find_all('a', attrs={'class': 'drive-name'})

print(ssd)
