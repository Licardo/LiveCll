from base.net_get import NetGet
from parser_rule.html_parser_plugin import SoupBeautifulParser
from parser_rule.rule import Rule


if __name__ == '__main__':
    rules = [{'p1': 'div', 'p2': 'id', 'p3': 'js_content', 'p0': 'find'},
             {'p1': 'section', 'p2': 'style', 'p3': 'box-sizing: border-box;', 'p0': 'find'},
             {'p1': 'a', 'p0': 'find_all', 'child': [{'p1': 'span', 'p0': 'find'}]}]
    url = 'https://mp.weixin.qq.com/s/mGZYpTfhLNaC1HSux23nvQ'
    header = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
              'Proxy-Connection': 'keep-alive'}
    get = NetGet()
    str_json = get.get(url, header=header)
    r = Rule()
    parser = SoupBeautifulParser(str_json, 'html.parser')
    sin, mul = r.parse(parser.get_parser(), rules, parser)
    print(sin)
    for span in mul:
        print(span.get_text())
    print(len(mul))

