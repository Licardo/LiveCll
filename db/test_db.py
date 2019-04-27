from db import db_base
from zhongliuzixun import top_latest


class DbOperator:

    @staticmethod
    def insert(datas):
        db = db_base.DbBase.connect()
        cursor = db.cursor()
        index = 0
        for data in datas:
            # try:
            index += 1
            sql = 'insert into cll (id, title, sub_title, url, image, image_urls, description, source, platform, ' \
                  'level, top, type) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ) '
            cursor.execute(sql, (index, data['title'], data['sub_title'], data['url'], data['image'],
                                 data['image_urls'], data['description'], data['source'], data['platform'],
                                 data['level'], data['top'], data['type']))
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
    def operate():
        lat = top_latest.TopLatest()
        datas = lat.loop_data(30)
        DbOperator.insert(datas)
        # DbOperator.query(2)


if __name__ == '__main__':
    DbOperator.operate()
