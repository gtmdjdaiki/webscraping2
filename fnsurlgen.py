#!/usr/bin/python
# coding: utf-8
#pythonの練習 2016/04/05 aizawadk
#FNSが記載されたテキストファイルを引数として読み込んだFNSのURLを生成するスクリプト
# command 引数１　引数２
#　引数１は対象のリスト　引数２は行数

import sys

URL1 = "https://eservice.fujitsu.com/supportdesk/oss/search/jfns/jfns"
URL2 = ".html"
FNAME = sys.argv[1]
LINE = sys.argv[2]

FLIST =  open (FNAME)
FNS =  FLIST.readlines()[int(LINE)]
print URL1+FNS[4:9]+URL2,
FLIST.close



