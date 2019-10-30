from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://www.pythonscraping.com/pages/warandpece.html")
bs0bj = BeautifulSoup(html)

nameList = bs0bj.findAll("span", {"class": "green"})
for name in nameList:
    print(name.get_text())
