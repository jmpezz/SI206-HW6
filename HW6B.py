from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

url = input('Enter URL: ')
count = int(input('Enter Count: '))
position = int(input('Enter Position: '))
list_name = []
f_list_name = []

for x in range(count):
	html = urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	url = soup.find_all('a')[position - 1].get('href')
	list_name.append(url)
	print ('Retrieving: ', url)