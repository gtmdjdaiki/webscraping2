#/bin/bash
#
#PyghonによるWebスクレイピング実装に向けての練習用シェルスクリプト
#富士通基盤保守のFNSをスクレイピングし、月例のNFS精査の自動化を目論む
# 1.htmlのダウンロード自動化
#2016/04/05
#aizawadk

if [ $# -ne 1 ]; then
    echo "指定された引数は$#個です。" 1>&2
    echo "実行するには1個の引数が必要です。" 1>&2
    exit 1
fi

LINE=`awk 'END{print NR}' $1`
COUNT=0
USER=`cat user.txt`
PASS=`cat pass.txt`

while [ $COUNT -ne $LINE ]
do
    COUNT=`expr $COUNT + 1`
    URL=`python fnsurlgen.py $1 $COUNT`
    wget --http-user=$USER --http-passwd=$PASS $URL
    sleep 2 
done

