import pymysql
from db import db_constant


class DbBase:
    @staticmethod
    def connect():
        db = pymysql.connect(db_constant.HOST, db_constant.USER, db_constant.PW, db_constant.DATABASE)
        return db
