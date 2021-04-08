# import pymysql
# from db import db_constant
import sqlite3
import os.path


class DbBase:
    @staticmethod
    def connect():
        # warning: 必须用绝对路径
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qrz.db")
        db = sqlite3.connect(path)
        return db


if __name__ == '__main__':
    print(os.path.join(os.path.dirname(os.path.abspath(__file__)), "qrz.db"))
