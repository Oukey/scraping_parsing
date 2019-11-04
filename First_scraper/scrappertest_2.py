from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.pythonscraping.com/pages/page3.html")
bs0bj = BeautifulSoup(html)

for child in bs0bj.find("table", {"id": "giftList"}).children:
    print(child)

