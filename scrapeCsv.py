#!/usr/bin/env python
# encoding:utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

html = open("jfns22978.html",'r',encoding='eucjp')
bsObj = BeautifulSoup(html,"html.parser")
table = bsObj.find_all("table",{"id":"tbl_prdct"})[0]
rows = table.find_all("tr")
csvFile = open("./jfns22978.html.csv",'wt',newline='',encoding='utf-8')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.find_all(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()

