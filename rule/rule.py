from bs4 import BeautifulSoup
from base.net_get import NetGet


class Rule(object):

    # 规则示例
    # 规则结构：最外层是一个数组，每一项是一个字典，如果字典有子项，子项也是一套完整规则
    # 最后一位 0：代表调用find()方法，1：代表调用find_all()方法，2：代表同级的字典
    # 字典项介绍：
    # p1 代表元素 比如<div> <a> <span>等等
    # p2 代表元素的属性名称 目前只支持 id、class、style
    # p3 代表元素属性的具体值
    # p0 代表调用解析html引擎的方法名 目前支持 find() find_all() dict['']
    # child 代表该规则下面有子规则，子规则的定义和父规则一致
    # todo 问题：目前只支持解析某一个元素的数据，对应数据库也就是只能解析出一个字段  需要扩展
    rules = [{'p1': 'div', 'p2': 'id', 'p3': 'js_content', 'p0': 'find'},
             {'p1': 'section', 'p2': 'style', 'p3': 'box-sizing: border-box;', 'p0': 'find'},
             {'p1': 'a', 'p0': 'find_all', 'child': [{'p1': 'href', 'p0': 'dict'}]}]

    def parse(self, soup, rules):
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
                    f, all = self.parse(soup, rules)
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
    rule = Rule()
    rel, rels = rule.parse(soup, rule.rules)
    print(rels)
    print(len(rels))
