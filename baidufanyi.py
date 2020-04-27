# encoding: utf-8
# baidufanyi.py

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json
import md5
import urllib
import random
import httplib

# 免费申请百度翻译API https://api.fanyi.baidu.com/
# 在控制台获取APPID与密钥
APPID = '' #APPID
KEY = '' #密钥

# VNR传入的语言参数与百度api不同，请手动修改
# https://api.fanyi.baidu.com/api/trans/product/apidoc
FROM = 'auto' #源语言
TO = 'zh' #目标语言

def translate(text, to='zh', fr='auto'):
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = urllib.quote(text.encode('utf8'))
    fromLang = FROM
    toLang = TO
    salt = random.randint(32768, 65536)
    sign = APPID+text+str(salt)+KEY
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+APPID+'&q='+q+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    
    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        r = httpClient.getresponse().read()
        return json.loads(r)['trans_result'][0]['dst']
    except Exception, e:
        print e

if __name__ == "__main__":
  #s = u"こんにちは？"
  s = u"apple"
  t = translate(s, to='zh', fr='auto')
  print t