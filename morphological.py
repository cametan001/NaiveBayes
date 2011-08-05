#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import urllib, urllib2, os.path
from BeautifulSoup import BeautifulSoup

# 'Yahoo!デベロッパーズネットワークのアプリケーションIDをAppIDと言う別ファイルに保存しておく
f = open(os.path.join(os.path.dirname(__file__), 'AppID'), 'r')
appid = f.readline().rstrip()
f.close()
pageurl = "http://jlp.yahooapis.jp/MAService/V1/parse"

# Yahoo!形態素解析の結果をリストで返します。
def split(sentence, appid = appid, results = "ma", filter = "1|2|3|4|5|9|10"):
    sentence = sentence.encode('utf-8')
    params = urllib.urlencode({'appid' : appid, 'results' : results, 'filter' : filter, 'sentence' : sentence})
    results = urllib2.urlopen(pageurl, params)
    soup = BeautifulSoup(results.read())

    return [w.surface.string for w in soup.ma_result.word_list]

# if __name__ == '__main__':
#     for i in split(u'庭には二羽にわとりがいる'):
#         print i,
