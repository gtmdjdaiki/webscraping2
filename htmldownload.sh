#/bin/bash
#
#PyghonによるWebスクレイピング実装に向けての練習用シェルスクリプト
#富士通基盤保守のFNSをスクレイピングし、月例のNFS精査の自動化を目論む
# 1.htmlのダウンロード自動化
#2016/04/05
#aizawadk

LINE=`awk 'END{print NR}' fnslist.txt`
COUNT=0
USER=hoge
COUNT=hoge
while [ $COUNT -ne $LINE ]
do
    COUNT=`expr $COUNT + 1`
    URL=`python fnsurlgen.py fnslist.txt $COUNT`
    wget --http-user=$USER --http-passwd=$PASS $URL
#    python fnsurlgen.py fnslist.txt $COUNT
    sleep 2 
done

