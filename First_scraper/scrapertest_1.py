from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs0bj = BeautifulSoup(html)

# allText = bs0bj.findAll(id="text")
allText = bs0bj.findAll("", {"id": "text"})
print(allText)

nameList0 = bs0bj.findAll(text='the prince')
print(len(nameList0))
nameList = bs0bj.findAll("span", {"class": "green"})
for name in nameList:
    print(name.get_text())
