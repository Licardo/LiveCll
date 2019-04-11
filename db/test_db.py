import pymysql
from zhongliuzixun import top_latest


def connect():
    lat = top_latest
    datas = lat.loop_data(30)

    db = pymysql.connect('localhost', 'root', 'zh326159', 'qrz')
    cursor = db.cursor()
    index = 0
    for data in datas:
        # try:
        index += 1
        cursor.execute('insert into cll_test(id, title, detail) values (%s, %s, %s) ', (index, data[0], data[1]))
        db.commit()
        # except pymysql.err.ProgrammingError:
        #     db.rollback()
    cursor.close()
    db.close()


if __name__ == '__main__':
    connect()