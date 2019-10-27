from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    '''Функция возвращает название страницы или None'''
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs0bj = BeautifulSoup(html.read())
        title = bs0bj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title is None:
    print('Название не найдено')
else:
    print(title)
