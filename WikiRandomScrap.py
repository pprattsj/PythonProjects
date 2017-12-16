import bs4
from urllib.request import urlopen as uReg
from bs4 import BeautifulSoup as soup
myurl ='https://en.wikipedia.org/wiki/Special:Random'

def wikiRandom():
 uClient = uReg(myurl)
 page_html = uClient.read()
 page_soup = soup(page_html,"html.parser")
 page_soup.body.span
 desc = page_soup.p.text
 title = page_soup.h1.text
 return title, desc.split('.')[0]

def wikiThoughts(y):
 import textwrap as tw
 x=0
 while x<y:
  wiki = wikiRandom()
  print(wiki[0])
  desc = tw.wrap(wiki[1])
  for z in desc:
   print(z)
  print('\n')
  x=x+1
 
