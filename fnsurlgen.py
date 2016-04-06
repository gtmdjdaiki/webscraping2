#!/usr/bin/python
# coding: utf-8
#pythonの練習 2016/04/05 aizawadk
#FNSが記載されたテキストファイルを引数として読み込んだFNSのURLを生成するスクリプト
# command 引数１　引数２
#　引数１は対象のリスト　引数２は行数

import sys

def main():
    URL1 = "https://eservice.fujitsu.com/supportdesk/oss/search/jfns/jfns"
    URL2 = ".html"
    args = sys.argv
    arglen = len(args)

    if (arglen != 3):
        print "Usage: Python %s filename linenumber" %args[0]
        quit()

    with open (args[1]) as FLIST:
        FNS =  FLIST.readlines()[int(args[2])]
        print URL1+FNS[4:9]+URL2

if __name__ == '__main__':
    main()
