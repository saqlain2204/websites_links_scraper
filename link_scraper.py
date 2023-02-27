import requests
import html5lib
from bs4 import BeautifulSoup

url=input("Enter the URL from where the links are to be scraped\n")
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
anchors=soup.find_all('a')
links=set()
for link in anchors:
    if(link.get_text('href') != '#'):
        link=url+"/"+link.get_text('href')+"/"
        links.add(link)
links=list(links)
for each_link in links:
    print(each_link)
