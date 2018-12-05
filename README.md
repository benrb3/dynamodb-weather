The data.csv file is a data dump from the sqlite3 weather database.
Steps to get this on the Rpi2:
$ cd ~/WX/sqlite3/db
$ sqlite3 wxdata.db
> .headers on
> .mode csv
> .output data.csv
> select * from t1;
> .quit

Next:

Start python virtual environment:
$ source bin/activate

Create table if necessary:
$ python3 dynamodb-create-table.py
  to create the 'WeatherData' table

Clean up the data file. This removes rows with missing values and
removes duplicate rows. It also splits the timestring into
'yyyy-mm-dd' and 'time' cells. This will create a 'data-clean.csv' file.
$ python3 clean-csv-file.py

Writes data in 'data-clean.csv' to table 'WeatherData':
$ python3 write-data.py

Query the table:
$ python3 query-dynamodb.py
