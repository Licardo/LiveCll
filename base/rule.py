from bs4 import BeautifulSoup
from base.net_get import NetGet


# 规则
# 最后一位 0：代表调用find()方法，1：代表调用find_all()方法，2：代表同级的字典
rules = [{'p1': 'div', 'p2': 'id', 'p3': 'js_content', 'p0': 'find'},
         {'p1': 'section', 'p2': 'style', 'p3': 'box-sizing: border-box;', 'p0': 'find'},
         {'p1': 'a', 'p0': 'find_all', 'child': [{'p1': 'href', 'p0': 'dict'}]}]


def parse(soup, rules):
    rels = list()
    for rule in rules:
        flag = rule['p0']
        if flag == 'find':
            if len(rule) == 2:
                soup = soup.find(rule['p1'])
            elif len(rule) == 4:
                if rule['p2'] == 'id':
                    soup = soup.find(rule['p1'], id=rule['p3'])
                elif rule['p2'] == 'class_':
                    soup = soup.find(rule['p1'], class_=rule['p3'])
                elif rule['p2'] == 'style':
                    soup = soup.find(rule['p1'], style=rule['p3'])
        elif flag == 'find_all':
            items = list()
            if len(rule) == 2 or len(rule) == 3:
                items = [a for a in soup.find_all(rule['p1'])]
            elif len(rule) == 4:
                if rule[1] == 'id':
                    items = soup.find_all(rule[0], id=rule[2])
                elif rule[1] == 'class_':
                    items = soup.find_all(rule[0], class_=rule[2])
                elif rule[1] == 'style':
                    items = soup.find_all(rule[0], style=rule[2])
            for soup in items:
                rules = rule['child']
                f, all = parse(soup, rules)
                rels.append(f)
        elif flag == 'dict':
            soup = soup[rule['p1']]
    return soup, rels


if __name__ == '__main__':
    url = 'https://mp.weixin.qq.com/s/mGZYpTfhLNaC1HSux23nvQ'
    header = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
              'Proxy-Connection': 'keep-alive'}
    get = NetGet()
    str_json = get.get(url, header=header)
    soup = BeautifulSoup(str_json, 'html.parser')
    rel, rels = parse(soup, rules)
    print(rels)
    print(len(rels))
