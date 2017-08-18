# Logs Analysis


## Running

* Make sure you have `newsdata.sql`, the SQL script file with all the data. It can be downloaded from the Udacity course page.

* Then run the following command to execute it in `news` database. You might have to create the database before-hand.

```sh
psql -d news -f newsdata.sql
```

* Finally run the script.

```sh
python2 get_database_report.py
```

* It will present you with necessary stats.

----
