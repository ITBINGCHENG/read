#B()用execjs模块编译3.js并执行hy函数，hy函数运用child_process调用2.js函数存储弹幕到数据库
#A()打开数据库读取最新的弹幕并使用pyttsx3模块将弹幕转换为语音
#注意将huya模块放入项目目录下
import execjs
import pyttsx3
import pymysql
import time
import _thread


def A():
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "huya")  # 连接到虎牙弹幕数据库

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    engine = pyttsx3.init()
    engine.setProperty('rate', 500)  # 调节语速

    content = ""
    # SQL 查询语句
    sqlii = "select max(ID) from danmu2019年1月29日"  # 获取最大ID值
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

def B():
    with open("3.js",'r', encoding='UTF-8') as f:
        jsData = f.read()
    # e是 baidujs.js 的一个js 函数
    execjs.compile(jsData).call('hy',['11342412']) #此处hy函数传递的参数为js数组,[]形式



# 创建两个线程
try:
   _thread.start_new_thread( A,() )#A()打开数据库读取最新的弹幕并使用pyttsx3模块将弹幕转换为语音
   _thread.start_new_thread( B,() )#B()用execjs模块编译3.js并执行hy函数，hy函数运用child_process调用2.js函数存储弹幕到数据库
except:
   print ("Error: 无法启动线程")

while 1:    #函数多线程要加这句话，维持程序不会直接结束程序，不能执行多进程
   pass