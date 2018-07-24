# encoding=utf-8
from db import MyCon


class BaseDao:
    mycol = None;
    def __init__(self,collectionName,documentName):
        conn = MyCon.MyCon()
        con = conn.conn()
        mycol = con[collectionName][documentName]

    def saveList(self,mylist):
        self.mycol.insert_many(mylist);

    def deleteList(self,mylist):
        self.mycol.delete_many(mylist)

    def updateList(self,mylist):
        self.mycol.update_many(mylist)

    def findList(self,mylist):
        self.mycol.find()