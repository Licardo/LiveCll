from abc import ABC, abstractmethod


class HtmlParser(ABC):
    @abstractmethod
    def find(self, soup, element, key=None, value=None):
        pass

    @abstractmethod
    def find_all(self, soup, element, key=None, value=None):
        pass
