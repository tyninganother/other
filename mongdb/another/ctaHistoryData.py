# encoding: UTF-8

# """
# 本模块中主要包含：
# 1. 将MultiCharts导出的历史数据载入到MongoDB中用的函数
# 2. 将通达信导出的历史数据载入到MongoDB中的函数
# 3. 将交易开拓者导出的历史数据载入到MongoDB中的函数
# 4. 将OKEX下载的历史数据载入到MongoDB中的函数
# """
#
# import csv
# from datetime import datetime, timedelta
# from time import time
#
# import pymongo
#
# from vnpy.trader.vtObject import VtTickData
#
# dbName = 'dbName_test'
# symbol = 'symbol_test'
# mongoHost = '127.0.0.1'
# mongoPort = 27017
#
# from vnpy.trader.app.ctaStrategy import ctaBacktesting
#
#
# ctaBacktesting().roundToPriceTick(1,2);
#
# def loadTbPlusCsv(fileName):
#     """将TB极速版导出的csv格式的历史分钟数据插入到Mongo数据库中"""
#     """将TB极速版导出的csv格式的历史分钟/Tick数据插入到Mongo数据库中"""
#     start = time()
#     print u'开始读取CSV文件%s中的数据插入到%s的%s中' % (fileName, dbName, symbol)
#
#     print '开始读取CSV%s文%s件%s中' % (fileName, dbname, sols)
#     f = open(fileName, 'r')
#     reader = csv.reader(f)
#
#     # 锁定集合，并创建索引
#     client = pymongo.MongoClient(mongoHost, mongoPort)
#     collection = client[dbName][symbol]
#     collection.ensure_index([('datetime', pymongo.ASCENDING)], unique=True)
#
#     # 读取数据和插入到数据库
#     print 'dsafdsafdsa',fileName
#     reader = csv.reader(file(fileName, 'r'))
#
#     f = open(fileName, 'r')
#     reader = csv.reader(f)
#
#     count = 0
#     for d in reader:
#         bar = VtTickData()
#         bar.vtSymbol = symbol
#         bar.symbol = symbol
#         # 成交数据
#         bar.lastPrice = d[4]  # 最新成交价
#         bar.lastVolume = None  # 最新成交量
#         bar.volume = None  # 今天总成交量
#         bar.openInterest = None  # 持仓量
#         bar.date = d[0]
#         timeStr = "0.0" if d[20] == "0" else d[20]
#         # # 用0在后面补全
#         bar.datetime = datetime.strptime(
#             d[0].replace('\xef\xbb\xbf', '') + " " + timeStr.replace(':', '') + "0" * (8 - len(timeStr)) + '.000',
#             "%Y%m%d %H%M%S.%f")
#         bar.time = bar.datetime.strftime('%H:%M:%S.%f')  # 11:20:56.5
#         #
#         # # 常规行情
#         bar.openPrice = float(d[8])  # 今日开盘价
#         bar.highPrice = float(d[9])  # 今日最高价
#         bar.lowPrice = float(d[10])  # 今日最低价
#         bar.preClosePrice = None
#         #
#         bar.upperLimit = float(d[15])  # 涨停价
#         bar.lowerLimit = float(d[16])
#         flt = {'datetime': bar.datetime}
#         # newdatetime = collection.find_one(flt)
#         # # print newdatetime['datetime'].strftime("%Y-%m-%d %H:%M:%S.%f")
#         # if newdatetime is not None :
#         #     bar.datetime = datetime.strptime(d[0].replace('\xef\xbb\xbf', '') + " " + timeStr.replace(':', '') + "0" * (8 - len(timeStr)) + '.500',"%Y%m%d %H%M%S.%f")
#         #     print bar.datetime
#         collection.update_one({'datetime': bar.datetime}, {'$set': bar.__dict__}, upsert=True)
#
#         count += 1
#         if count % 10000 == 0:
#             print bar.date, bar.time
#
#     print u'插入完毕，耗时：%s' % (time() - start)
#     print u'数据总量:%s' % (count)
#
#
# # loadTbPlusCsv();
#
# from itertools import islice
# def loadTbPlusCsv(fileName):
#     print '开始读取CSV文件%s中' % fileName
#     f = open(fileName,'r')
#     reader = csv.reader(f)
#     # for d in islice(reader, 1, None):
#     for d in reader:
#         print d
# import os
# #
# #
# def file_name(file_dir):
#     for root, dirs, files in os.walk(file_dir):
#         for file in files:
#             if os.path.splitext(file)[1] == '.csv':
#                 realpath =root + os.path.basename(file)
#                 print realpath
#                 print loadTbPlusCsv(realpath)
# file_name('/Users/haining/Desktop/myproject/mongodb/');
# #
# #
# #
# # list1 = [0,22,32,22,34,22]
# # list2 = [1,2,5,2,33,2]
# # kkk = 0
# # count = 0
# # for d in list1:
# #     # print list1[count] >= list2[count]
# #     if list1[count] < list2[count]:
# #         kkk = kkk + 1
# #     print kkk < 0
# #     count = count + 1

class FFFF:
    vadss = 0
    vadss1 = 0
    vadss2 = 0
    vadss3 = 0
    vadss4 = 0

    # def __init__(self):
    #     vadss = 2
    #     print 'fdsafds' ,vadss,'fdsafdsdsafda'
    # def __init__(self):
    #     vadss = 1
    #     print 'fdsafds' ,vadss
    def __init__(self,ffff):
        vadss = 1
        print 'fdsafds' ,vadss,ffff
    def __init__(self,ffdsff):
        vadss = 1
        print 'fdsafds' ,vadss

    def dsadas1(self,dsa):
        print 'dsadas' ,self.vadss
        return self.vadss
    def dsadas2(self,dsa):
        print 'dsadas' ,self.vadss
        return self.vadss
    def dsadas3(self,dsa):
        print 'dsadas' ,self.vadss
        return self.vadss

print FFFF('dsasdsa');
FFFF('dsasdsa').dsadas1('fdsafda');
FFFF('dsasdsa').dsadas1('fdsafda');
FFFF('dsasdsa').dsadas1('fdsafda');
FFFF('dsasdsa').dsadas1('fdsafda');
FFFF('dsasdsa').dsadas1('fdsafda');
# vvvv.dsadas();
