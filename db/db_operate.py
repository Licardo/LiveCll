from db import db_base


class DbOperator:

    @staticmethod
    def insert(datas):
        db = db_base.DbBase.connect()
        cursor = db.cursor()
        index = DbOperator.query_size(cursor)
        for data in datas:
            if DbOperator.find_data_for_url(cursor, data.url) == 0:
                # 如果数据库中不存在改调数据，执行插入操作
                # try:
                index += 1
                sql = 'insert into cll (id, title, sub_title, url, image, image_urls, description, source, platform, ' \
                      'level, top, type) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ) '
                cursor.execute(sql, (index, data.title, data.sub_title, data.url, data.image,
                                     data.image_urls, data.description, data.source, data.platform,
                                     data.level, data.top, data.type))
                db.commit()
                # except pymysql.err.ProgrammingError:
                #     db.rollback()
        cursor.close()
        db.close()

    @staticmethod
    def query(page_index):
        if page_index < 1:
            return None
        page_size = 30
        sql = 'select * from cll_test where id < %d and id >= %d' % (page_index*page_size, (page_index-1)*page_size)
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
    def query_size(cursor):
        sql = 'select count(*) from cll'
        cursor.execute(sql)
        result = cursor.fetchone()
        return result[0]


if __name__ == '__main__':
    db = db_base.DbBase.connect()
    cursor = db.cursor()
    DbOperator.find_data(cursor, 'https://doctor.liangyihui.net/#/doc/49107')
