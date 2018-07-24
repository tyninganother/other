# encoding=utf-8
from pymongo import MongoClient
import constant


class MyCon:
    conn = None

    def conn(self):
        return self.new_conn(constant.LOCAL_DB_HOST, constant.LOCAL_DB_PORT)

    def __init__(self):
        global conn
        conn = None;

    def new_conn(self, db_host, db_port):
        global conn
        if conn is None:
            conn = MongoClient(db_host, db_port);
        return conn;
