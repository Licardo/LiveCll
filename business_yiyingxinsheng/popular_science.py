from base import net_get
from parser_rule import rule, html_parser_plugin
from db import db_info, db_operate
from base.base import Base

# 亿迎新生-科普专栏
from parser_rule.html_parser import HtmlParser


class PopularScience(Base):

    rules = [{'p0': 'find', 'p1': 'div', 'p2': 'class_', 'p3': 'containers'},
             {'p0': 'find', 'p1': 'div', 'p2': 'class_', 'p3': 'pages js_show'},
             {'p0': 'find', 'p1': 'div', 'p2': 'class_', 'p3': 'bd'},
             {'p0': 'find', 'p1': 'div', 'p2': 'class_', 'p3': 'list-view'},
             {'p0': 'find_all', 'p1': 'a'}]
    child_rule1 = [{'p0': 'find', 'p1': 'div', 'p2': 'class_', 'p3': 'weui-media-box__hd'},
                   {'p0': 'find', 'p1': 'img'}]
    child_rule2 = [{'p0': 'find', 'p1': 'div', 'p2': 'class_', 'p3': 'weui-media-box__bd'}]

    url = 'http://papweixin.ilvzhou.com/article/index?config_id=14&column_id=387'

    header = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
              'Proxy-Connection': 'keep-alive'}

    def get_html(self):
        get = net_get.NetGet()
        str_json = get.get(self.url, header=self.header)
        rul = rule.Rule()
        parser = html_parser_plugin.SoupBeautifulParser(str_json, 'html.parser')
        sin, mul = rul.parse(parser.get_parser(), self.rules, parser)
        return self.handle_datas(mul, parser)

    def handle_datas(self, datas, parser: HtmlParser = None):
        info_list = list()
        rul = rule.Rule()
        for doc in datas:
            csin, cmul = rul.parse(doc, self.child_rule1, parser)
            div, divs = rul.parse(doc, self.child_rule2, parser)
            info = db_info.DbInfo()
            info.title = div.find('h4').get_text()
            info.image = 'http://papweixin.ilvzhou.com' + csin['src']
            info.image_urls = ''
            info.description = ''
            info.source = '亿迎新生患者关爱中心'
            info.platform = '科普专栏'
            info.level = 2
            info.top = False
            info.url = 'http://papweixin.ilvzhou.com' + doc['href']
            info.type = '无'
            info.sub_title = div.find('p').get_text()
            info_list.append(info)
        return info_list


if __name__ == '__main__':
    science = PopularScience()
    datas = science.get_html()
    operate = db_operate.DbOperator()
    operate.insert(datas)
