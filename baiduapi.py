'''
使用百度语音api实现转文字为语音功能，此py只能生成MP3文件，
尚不能直接读出所输入的文字
'''
from aip import AipSpeech
# 百度api要联网
""" 你的 APPID AK SK """
import settings
API_KEY = settings.API_KEY
APP_ID = settings.APP_ID
SECRET_KEY = settings.SECRET_KEY

with open('wenzi.txt','r',encoding='UTF-8') as f:
    txt = f.read()
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
result = client.synthesis(txt, 'zh', 1, {'spd':5,
    'vol': 5, 'per': 4
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)