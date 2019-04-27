from db import db_operate
from zhongliuzixun import top_latest


class DbOperator:

    @staticmethod
    def operate():
        lat = top_latest.TopLatest()
        datas = lat.loop_data(30)
        db_operate.DbOperator.insert(datas)
        # DbOperator.query(2)


if __name__ == '__main__':
    DbOperator.operate()
