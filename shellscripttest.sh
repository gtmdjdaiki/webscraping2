#/bin/bash
#
#PyghonによるWebスクレイピング実装に向けての練習用シェルスクリプト
#富士通基盤保守のFNSをスクレイピングし、月例のNFS精査の自動化を目論む
# 1.htmlのダウンロード自動化
# 2.patch情報などのデータの整形と対処すあーばに該当するpatchのピックアップなど
#2016/04/04
#aizawadk

LINE=`awk 'END{print NR}' fnslist.txt`
COUNT=0
echo ${LINE}
FNSNO=11126

python fnsurlgen.py fnslist.txt 1
URL="https://eservice.fujitsu.com/supportdesk/oss/search/jfns/jfns$FNSNO.html"
echo ${URL}
while [ $COUNT -ne $LINE ]
do
    COUNT=`expr $COUNT + 1`
    echo ${COUNT}
    sleep 1 
done

