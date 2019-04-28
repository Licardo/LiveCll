from base.net_get import NetGet
from parser_rule.rule import Rule
from parser_rule.html_parser_plugin import SoupBeautifulParser
from db import db_info
from db import db_operate


# 淋巴瘤之家-专家说
class ProfessionalPoint(NetGet):

    @staticmethod
    def get_html():
        url = 'https://mp.weixin.qq.com/s/mGZYpTfhLNaC1HSux23nvQ'
        header = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 '
                                '(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                  'Proxy-Connection': 'keep-alive'}
        get = NetGet()
        str_json = get.get(url, header=header)
        rules = [{'p1': 'div', 'p0': 'find', 'p2': 'id', 'p3': 'js_content'},
                 {'p0': 'find', 'p1': 'section', 'p2': 'style', 'p3': 'box-sizing: border-box;'},
                 {'p0': 'find_all', 'p1': 'a'}]
        rule = Rule()
        parser = SoupBeautifulParser(str_json, 'html.parser')
        sin, mul = rule.parse(parser.get_parser(), rules, parser)
        info_list = list()
        for a in mul:
            info = db_info.DbInfo()
            info.title = a.find('span').get_text()
            info.image = 'https://mmbiz.qpic.cn/mmbiz_jpg/y4URaX8bynLyznbzl9Ek2hL0ASLsaMV6FJ8sZicnLD0KfZ9GFJpibLiaA' \
                         'l6nOBFKtRB20XC3W3iarHQCJ6fzddremw/640?wx_fmt=jpeg'
            info.image_urls = ''
            info.description = ''
            info.source = '淋巴瘤之家'
            info.platform = '专家说'
            info.level = 2
            info.top = False
            info.url = a['href']
            info.type = '无'
            info.sub_title = ''
            info_list.append(info)
        return info_list


if __name__ == '__main__':
    datas = ProfessionalPoint.get_html()
    operate = db_operate.DbOperator()
    operate.insert(datas)
