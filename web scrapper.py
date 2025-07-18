import requests
from bs4 import BeautifulSoup

url = input()
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for tag in soup.find_all('a'):
    print(tag.get('href'))
