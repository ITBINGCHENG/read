"""此项目使用execjs模块运行js文件，1.js需要的node模块需要和js文件放在同一项目文件夹里
execjs使用需要本机有运行js文件的环境"""

import execjs

with open("1.js",'r', encoding='UTF-8') as f:
    jsData = f.read()
# e是 baidujs.js 的一个js 函数
p = execjs.compile(jsData).call('client.start') #执行1.js中的client.start方法
