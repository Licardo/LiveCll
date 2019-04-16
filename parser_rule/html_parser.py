from abc import ABC, abstractmethod


class HtmlParser(ABC):
    def __init__(self, json, type):
        self.json = json
        self.type = type

    @abstractmethod
    def find(self, soup, element, key=None, value=None):
        pass

    @abstractmethod
    def find_all(self, soup, element, key=None, value=None):
        pass

    @abstractmethod
    def get_parser(self):
        return None
