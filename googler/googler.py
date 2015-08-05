#use python 2.7

import time
import urllib
import mechanize
from BeautifulSoup import BeautifulSoup
import re

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders=[('User-agent','chrome')]

term = "Blade Runner".replace(" ","+")
query = "http://www.google.com/search?num=5&q="+term+"&ie=UTF-8"

htmltext = br.open(query).read()

#print htmltext

soup = BeautifulSoup(htmltext)

search = soup.findAll('div',attrs={'id':'ires'})

searchtext = str(search[0])

soup1 = BeautifulSoup(searchtext)
list_items = soup1.findAll('h3')
#regex = "q(?!.*q).*?&amp"
#pattern = re.compile(regex)

for h3 in list_items:
	soup2 = BeautifulSoup(str(h3))
	links = soup2.findAll('a')	
	#source_link = links[0]
	#print source_link
	#source_url = re.findall(pattern, str(source_link))
	if len(links)>0:
		i = 0
		while i < len(links):
			print links[i] #.replace("q=","").replace("&amp","")
			i = i +1