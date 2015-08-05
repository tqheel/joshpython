import time
import urllib
import mechanize
from BeautifulSoup import BeautifulSoup
import re

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders=[('User-agent','chrome')]

term = "Blade Runner".replace(" ","+")
query = "https://www.google.com/search?num=5&q="+term

htmltext = br.open(query).read()

#print htmltext

soup = BeautifulSoup(htmltext)

search = soup.findAll('div',attrs={'id':'search'})

searchtext = str(search[0])

soup1 = BeautifulSoup(searchtext)
list_items = soup1.findAll('li')
regex = "q(?!.*q).*?&amp"
pattern = re.compile(regex)

for li in list_items:
	soup2 = BeautifulSoup(str(li))
	links = soup2.findAll('a')	
	source_link = links[0]
	source_url = re.findall(pattern, str(source_link))
	if len(source_url)>0:
		print source_url[0].replace("q=","").replace("&amp","")