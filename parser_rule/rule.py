from parser_rule.html_parser import HtmlParser


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
             {'p1': 'a', 'p0': 'find_all', 'child': [{'p1': 'href&span', 'p0': 'dict&find'}]}]

    def parse(self, soup, rules, parser: HtmlParser):
        if rules is None:
            return None, None
        arrays = list()
        for rule_ in rules:
            flag = rule_['p0']
            if flag == 'find':
                soup = parser.find(soup, rule_['p1'], rule_.get('p2', None), rule_.get('p3', None))
            elif flag == 'find_all':
                items = parser.find_all(soup, rule_['p1'], rule_.get('p2', None), rule_.get('p3', None))
                for soup in items:
                    rules = rule_.get('child', None)
                    f, a = self.parse(soup, rules, parser)
                    arrays.append(f)
            elif flag == 'dict':
                soup = soup[rule_['p1']]
        return soup, arrays

