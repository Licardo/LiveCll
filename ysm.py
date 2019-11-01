from db.db_operate import DbOperator
from business_gongzhonghao.spider_gzh import SpiderGZH

def yangshenmiao():
    # 杨申淼的公众号
    name = '杨申淼'
    index = 0
    spider = SpiderGZH(name, index)
    DbOperator.insert(spider.handle_datas(spider.get_all_article()))


if __name__ == '__main__':
    yangshenmiao()