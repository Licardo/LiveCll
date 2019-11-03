from db import db_base


class DbOperator:

    @staticmethod
    def insert(datas):
        db = db_base.DbBase.connect()
        cursor = db.cursor()
        # index = DbOperator.query_size(cursor)
        for data in datas:
            if DbOperator.find_data_for_url(cursor, data.url) == 0:
                # 如果数据库中不存在该条数据，执行插入操作
                # try:
                # index += 1
                sql = 'insert into cll (title, sub_title, url, image, image_urls, description, source, platform, ' \
                      'level, top, type, send_time) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s) '
                cursor.execute(sql, (data.title, data.sub_title, data.url, data.image,
                                     data.image_urls, data.description, data.source, data.platform,
                                     data.level, data.top, data.type, data.send_time))
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
            sql = 'update cll set send_time = %s where url = %s'
            cursor.execute(sql, (data.send_time, data.url))
            db.commit()
        cursor.close()
        db.close()

    @staticmethod
    def query(page_index):
        if page_index < 1:
            return None
        page_size = 30
        sql = 'select * from cll where id < %d and id >= %d' % (page_index*page_size, (page_index-1)*page_size)
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
        sql = 'select * from cll where id >= %d and id <= %d' % (page_min, page_max)
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
        sql = "select count(*) from cll where url = '%s'" % url
        cursor.execute(sql)
        return cursor.fetchone()[0]

    @staticmethod
    def query_size(cursor=None):
        db = None
        if cursor is None:
            db = db_base.DbBase.connect()
            cursor = db.cursor()
        sql = 'select count(*) from cll'
        cursor.execute(sql)
        result = cursor.fetchone()
        if db is not None:
            cursor.close()
            db.close()
        return result[0]


if __name__ == '__main__':
    DbOperator.query(1)
