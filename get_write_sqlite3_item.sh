#!/bin/bash

DIR="/home/ben/tmp/sqlite3"
csvfile="$DIR/one-item.csv"
jsonfile="$DIR/one-item.json"

ssh pi@192.168.1.102 'sqlite3 -header /home/pi/WX/sqlite3/db/wxdata.db "SELECT * FROM t1 ORDER BY unixtime DESC LIMIT 1;"'|sed 's/|/,/g' > $csvfile
python3 $DIR/one-item.py

# check exit code of previous command for success
if [ $? -eq 0 ]; then
    /home/ben/.local/bin/aws dynamodb put-item --table-name WeatherData --item file://$jsonfile --endpoint-url http://localhost:8000
else
    exit
fi
