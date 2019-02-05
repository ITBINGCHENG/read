'''
此项目应用pyttsx3模块，
首先连接到弹幕数据库，此弹幕数据库使用js程序实时收集弹幕。py通过弹幕id找到最新的弹幕，然后循环读取新的id并在id更新后
将id对应的弹幕交给Pyttsx3模块直接输出语音
'''

import pyttsx3
import pymysql
import time
# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "huya")#连接到虎牙弹幕数据库

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
engine = pyttsx3.init()
engine.setProperty('rate', 500)#调节语速

content=""
# SQL 查询语句
sqlii="select max(ID) from danmu2019年1月29日"#获取最大ID值
cursor.execute(sqlii)
maxnumber=cursor.fetchall()
for row in maxnumber:
    n=int(row[0])
while True:
    try:
        # 执行SQL语句
        cursor.execute("SELECT * FROM danmu2019年1月29日 \
          WHERE ID > %s" % (n))
        db.commit()
        # 获取所有记录列表
        results = cursor.fetchall()
        if results :#判断结果是否为空
            for row in results:
                ID = row[0]
                name = row[1]
                content = content + ' ' + row[2]
                m = int(ID)
                if m > n:
                    n = m
        else:
            time.sleep(1)
        print(n)
        print(content)
        engine.say(content)
        content = ""
        # 注意，没有本句话是没有声音的
        engine.runAndWait()
    except:
        print ("Error: unable to fetch data")
        continue
    # 初始化， 必须要有奥



