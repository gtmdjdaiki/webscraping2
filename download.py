#!/usr/bin/env python
# coding:utf-8
#PyghonによるWebスクレイピング実装に向けての練習用シェルスクリプト
#富士通基盤保守のFNSをスクレイピングし、月例のNFS精査の自動化を目論む
# 1.htmlのダウンロード自動化
#2016/04/11
#aizawadk

import os
import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

#保存先となるディレクトリをファイル名まで指定
fout = open("filename","wb")

#プロキシ設定
proxies={"http":"http://user:pass@127.0.0.1:8080","https":"https://user:pass@127.0.0.1:8080"}

#ベーシック認証設定
auth = HTTPBasicAuth('user','pass')

#取得したいファイル名をURLで指定
url = "https://hoge.html"

r = requests.get(url=url,auth=auth,proxies=proxies)

#ファイルを変数dataに読み込み
fout.write(r.content)
fout.close()

