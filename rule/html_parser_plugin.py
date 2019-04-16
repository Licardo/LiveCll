from bs4 import BeautifulSoup
from rule.html_parser import HtmlParser


class SoupBeautifulParser(HtmlParser):
    soup = BeautifulSoup()

    def find(self, soup, element, key, value):
        if key is None:
            soup = soup.find(element)
        elif key == 'id':
            soup = soup.find(element, id=value)
        elif key == 'class_':
            soup = soup.find(element, class_=value)
        elif key == 'style':
            soup = soup.find(element, style=value)
        return soup

    def find_all(self, soup, element, key, value):
        items = list()
        if key is None:
            items = [a for a in soup.find_all(element)]
        elif key == 'id':
            items = soup.find_all(element, id=value)
        elif key == 'class_':
            items = soup.find_all(element, class_=value)
        elif key == 'style':
            items = soup.find_all(element, style=value)
        return items
