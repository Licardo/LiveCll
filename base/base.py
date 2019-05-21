from abc import ABC, abstractmethod
from parser_rule.html_parser import HtmlParser


class Base(ABC):

    @abstractmethod
    def handle_datas(self, datas, parser: HtmlParser = None):
        pass
