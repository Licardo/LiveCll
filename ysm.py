from db.db_operate import DbOperator
from bmob.operate_data import OperateData
from business_gongzhonghao.spider_gzh import SpiderGZH


def yangshenmiao():
    # 杨申淼的公众号
    name = '杨申淼'
    index = 0
    spider = SpiderGZH(name, index)
    DbOperator.insert(spider.handle_datas(spider.get_all_article()))


def database_bmob(start, end):
    ope = OperateData()
    ope.insert(ope.get_datas(start, end))


if __name__ == '__main__':
    start = DbOperator.query_size()
    print(str(start))
    yangshenmiao()
    end = DbOperator.query_size()
    print(str(start) + '===' + str(end))
    database_bmob(start, end)
