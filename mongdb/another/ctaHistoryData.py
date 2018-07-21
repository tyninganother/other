# encoding: UTF-8

"""
本模块中主要包含：
1. 将MultiCharts导出的历史数据载入到MongoDB中用的函数
2. 将通达信导出的历史数据载入到MongoDB中的函数
3. 将交易开拓者导出的历史数据载入到MongoDB中的函数
4. 将OKEX下载的历史数据载入到MongoDB中的函数
"""

import csv
from datetime import datetime, timedelta
from time import time

import pymongo

from vnpy.trader.vtObject import VtTickData


dbName = 'dbName_test'
symbol = 'symbol_test'
fileName = '/Users/haining/Desktop/myproject/mongodb/MA901_20180504.csv'
mongoHost = '127.0.0.1'
mongoPort = 27017



def loadTbPlusCsv():
    """将TB极速版导出的csv格式的历史分钟数据插入到Mongo数据库中"""
    """将TB极速版导出的csv格式的历史分钟/Tick数据插入到Mongo数据库中"""
    start = time()
    print u'开始读取CSV文件%s中的数据插入到%s的%s中' %(fileName, dbName, symbol)

     # 锁定集合，并创建索引
    client = pymongo.MongoClient(mongoHost, mongoPort)
    collection = client[dbName][symbol]
    collection.ensure_index([('datetime', pymongo.ASCENDING)], unique=True)

    # 读取数据和插入到数据库
    reader = csv.reader(file(fileName, 'r'))
    count = 0
    for d in reader:
        bar = VtTickData()
        bar.vtSymbol = symbol
        bar.symbol = symbol
        # 成交数据
        bar.lastPrice = d[4]  # 最新成交价
        bar.lastVolume = None  # 最新成交量
        bar.volume = None  # 今天总成交量
        bar.openInterest = None  # 持仓量
        bar.date = d[0]
        timeStr = "0.0" if d[20] == "0" else d[20]
        # # 用0在后面补全
        bar.datetime = datetime.strptime(d[0].replace('\xef\xbb\xbf','') + " " + timeStr.replace(':','') + "0" * (8 - len(timeStr)) + '.000',"%Y%m%d %H%M%S.%f")
        bar.time = bar.datetime.strftime('%H:%M:%S.%f')#11:20:56.5
        #
        # # 常规行情
        bar.openPrice = float(d[8])  # 今日开盘价
        bar.highPrice = float(d[9])  # 今日最高价
        bar.lowPrice = float(d[10])  # 今日最低价
        bar.preClosePrice = None
        #
        bar.upperLimit = float(d[15])  # 涨停价
        bar.lowerLimit = float(d[16])
        flt = {'datetime': bar.datetime}
        # newdatetime = collection.find_one(flt)
        # # print newdatetime['datetime'].strftime("%Y-%m-%d %H:%M:%S.%f")
        # if newdatetime is not None :
        #     bar.datetime = datetime.strptime(d[0].replace('\xef\xbb\xbf', '') + " " + timeStr.replace(':', '') + "0" * (8 - len(timeStr)) + '.500',"%Y%m%d %H%M%S.%f")
        #     print bar.datetime
        collection.update_one({'datetime': bar.datetime}, {'$set': bar.__dict__}, upsert=True)


        count += 1
        if count%10000==0:
            print bar.date, bar.time

    print u'插入完毕，耗时：%s' % (time()-start)
    print u'数据总量:%s' % (count)


loadTbPlusCsv();



