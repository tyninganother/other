# encoding: UTF-8

from csvutils import csvutil
from db import MyCon
import time
from vnpy.trader.VtBaseData import VtTickData

result = csvutil.readecsv('/Users/haining/Desktop/myproject/mongodb/MA901_20180503.csv');
for item in result:
    num = len(item)
    a = ''
    for i in item:
        if i == '':
            i = 'null'
        a = a + i
    print a;

conn = MyCon.MyCon();
con = conn.conn();
mycol = con['runoobdb']["sites"]
mycol.create_index('name1',unique=True)
mylist = [
    {"name1": "Taobao1","name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
    {"name1": "QQ1", "alexa": "101", "url": "https://www.qq.com"},
    {"name1": "Facebook1", "alexa": "10", "url": "https://www.facebook.com"},
    {"name1": "知乎1", "alexa": "103", "url": "https://www.zhihu.com"},
    {"name1": "Github1", "alexa": "109", "url": "https://www.github.com"}
]

x = mycol.insert_many(mylist)
x = mycol.insert(mylist)

print(x.inserted_ids)


def loadTbCsv(fileName, dbName, symbol):
    """将TradeBlazer导出的csv格式的历史分钟数据插入到Mongo数据库中"""
    import csv

    start = time()
    print u'开始读取CSV文件%s中的数据插入到%s的%s中' % (fileName, dbName, symbol)


    # 锁定集合，并创建索引
    # client = pymongo.MongoClient(globalSetting['mongoHost'], globalSetting['mongoPort'])
    conn = MyCon.MyCon();
    client = conn.conn();
    collection = client[dbName][symbol]
    collection.ensure_index([('datetime', 1)], unique=True)

    # 读取数据和插入到数据库
    reader = csv.reader(file(fileName, 'r'))
    for d in reader:
        bar = VtTickData()
        bar.vtSymbol = symbol
        bar.symbol = symbol
        bar.open = float(d[1])
        bar.high = float(d[2])
        bar.low = float(d[3])
        bar.close = float(d[4])
        bar.date = datetime.strptime(d[0].split(' ')[0], '%Y/%m/%d').strftime('%Y%m%d')
        bar.time = d[0].split(' ')[1] + ":00"
        bar.datetime = datetime.strptime(bar.date + ' ' + bar.time, '%Y%m%d %H:%M:%S')
        bar.volume = d[5]
        bar.openInterest = d[6]

        flt = {'datetime': bar.datetime}
        collection.update_one(flt, {'$set': bar.__dict__}, upsert=True)
        print bar.date, bar.time

    print u'插入完毕，耗时：%s' % (time() - start)
