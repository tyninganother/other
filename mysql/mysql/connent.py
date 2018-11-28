# -*- coding: UTF-8 -*-

import MySQLdb
import codecs

def addnbsp(slen):
    sss = ""
    while(len(sss)<=slen):
        sss = sss + " "
    return sss

def run():
    # 打开数据库连接
    db = MySQLdb.connect("10.10.1.253", "tianhaining", "TianTianTian", "summer_test", charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 使用execute方法执行SQL语句
    cursor.execute('select (497973 - count(*)) as "增加数量",count(*) as "剩余数量",TIMESTAMPDIFF(HOUR,"2018-08-23 12:53:56",now()) as "用时（小时)",(TIMESTAMPDIFF(MINUTE,"2018-08-23 12:53:56",now()) - (TIMESTAMPDIFF(HOUR,"2018-08-23 12:53:56",now())*60)) as "用时（分钟）",(497973 - count(*))/(TIMESTAMPDIFF(MINUTE,"2018-08-23 12:53:56",now())/30) as "每个30分钟处理数量",now() as "统计时间" from sp_invest_agreement where fdd_pdf_generate_status in(4)  order by id asc;')

    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchone()
    f = codecs.open('/Users/haining/invest_agreement.text', 'r+', encoding='utf-8')  # 必须事先知道文件的编码格式，这里文件编码是使用的utf-8
    content = f.read()  # 如果open时使用的encoding和文件本身的encoding不一致的话，那么这里将将会产生错误
    f.write("--------------------------------------------------------------------------\n")
    f.write("|" + addnbsp(len("增加数量") / 2 - len(str(data[0])) - 1) + str(data[0]) + "|" + addnbsp(
        len("剩余数量") / 2 - len(str(data[1]))) + str(+data[1]) + "|" + addnbsp(
        len("用时（小时)") / 2 - len(str(data[2]))) + str(data[2]) + "|" + addnbsp(
        len("用时（分钟）") / 2 - len(str(data[3])) - 1) + str(data[3]) + "|" + addnbsp(
        len("每个30分钟处理数量") / 2 - len(str(data[4]))) + str(data[4]) + "|" + addnbsp(
        len("统计时间") / 2 - len(str(data[5]))) + str(data[5]) + "\n")
    # 关闭数据库连接
    db.close()








