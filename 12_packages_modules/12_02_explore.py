"""
Getting plain text from wikipedia url

"""
from bs4 import BeautifulSoup
import requests

url = input('Please, type in a wikipedia url: ')
source = requests.get(url).text
soup = BeautifulSoup(source, features='html.parser')
name = soup.find('h1', {'id':'firstHeading'})
print(name.text)
for paragraph in soup.findAll('p'):
    print(paragraph.text)
