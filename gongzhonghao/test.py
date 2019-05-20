from gongzhonghao.spider_gzh import SpiderGZH
from db.db_operate import DbOperator

if __name__ == '__main__':
    name = '杨申淼'
    index = 0
    spider = SpiderGZH(name, index)
    datas = spider.get_all_article()
    # 插入数据库
    operator = DbOperator()
    operator.insert(spider.handle_data(datas))
