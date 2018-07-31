# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
def dbHandle():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        db='news',
        user='root',
        passwd='',
        charset='utf8',
    )
    return conn

class MyscrapyPipeline(object):
    def __init__(self):
        self.dbObject = dbHandle()
        self.cursor = self.dbObject.cursor()

    def process_item(self, item, spider):
        sql = 'insert into qiubai(name,news_id,url,text_content,has_image) values (%s,%s,%s,%s,%s)'
        try:
            self.cursor.execute(sql, (item['name'].encode("utf-8"), (item['news_id'].encode("utf-8"))[7:15],
                                      ("http://www.qiushibaike.com" + item['url'].encode("utf-8")),
                                      item['text_content'].encode("utf-8"), item['has_image'].encode("utf-8")))
            self.dbObject.commit()
        except Exception, e:
            print e
            self.dbObject.rollback()
        return item

    def __del__(self):
        self.cursor.close()
        self.dbObject.close()
