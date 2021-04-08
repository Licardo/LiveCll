from typing import List, Any

from db import db_base
from db import db_info
import os.path


class DbOperator:

    @staticmethod
    def insert(datas):
        db = db_base.DbBase.connect()
        cursor = db.cursor()
        for data in datas:
            if DbOperator.find_data_for_url(cursor, data.url) == 0:
                # 如果数据库中不存在该条数据，执行插入操作
                # try:
                sql = "insert into cll (title, sub_title, url, image, image_urls, description, source, platform, " \
                      "level, top, type, send_time) values " \
                      "('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}' ,'{}') "\
                    .format(data.title, data.sub_title, data.url, data.image,
                                     data.image_urls, data.description, data.source, data.platform,
                                     data.level, data.top, data.type, data.send_time)
                cursor.execute(sql)
                db.commit()
                # except pymysql.err.ProgrammingError:
                #     db.rollback()
        cursor.close()
        db.close()

    @staticmethod
    def update_time(datas):
        db = db_base.DbBase.connect()
        cursor = db.cursor()
        for data in datas:
            sql = "update cll set send_time = '{}' where url = '{}'".format(data.send_time, data.url)
            cursor.execute(sql)
            db.commit()
        cursor.close()
        db.close()

    @staticmethod
    def query(page_index):
        if page_index < 1:
            return None
        page_size = 30
        sql = "select * from cll where id < '{}' and id >= '{}'".format(page_index*page_size, (page_index-1)*page_size)
        db = db_base.DbBase.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        db.close()
        print(results)
        return results

    @staticmethod
    def query_for_row(page_min, page_max):
        if page_min < 1:
            return None
        if page_min > page_max:
            return None
        sql = "select * from cll where id >= '{}' and id <= '{}'".format(page_min, page_max)
        print(sql)
        db = db_base.DbBase.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        db.close()
        print(results)
        return results

    @staticmethod
    def find_data_for_url(cursor, url):
        sql = "select count(id) from cll where url = '{}'".format(url)
        cursor.execute(sql)
        return cursor.fetchone()[0]

    @staticmethod
    def query_size(cursor=None):
        db = None
        if cursor is None:
            db = db_base.DbBase.connect()
            cursor = db.cursor()
        sql = 'select count(id) from cll'
        cursor.execute(sql)
        result = cursor.fetchone()
        if db is not None:
            cursor.close()
            db.close()
        return result[0]


if __name__ == '__main__':
    infos= []
    for i in range(0, 9):
        info = db_info.DbInfo()
        info.title = str(i)
        infos.append(info)
    DbOperator.insert(infos)
    DbOperator.query(1)
