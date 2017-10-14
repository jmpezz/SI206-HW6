from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

url = input('Enter a url: ')
html = urlopen(url).read()
num_count = []

soup = BeautifulSoup(html, 'html.parser')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for tag in soup.find_all('span'):
	tag = str(tag)
	tags = tag.split('>')[1]
	split1 = tags.split('<')
	num_count.append(int(split1[0]))

print ("Count:", len(num_count))
print ("Sum:", sum(num_count))
