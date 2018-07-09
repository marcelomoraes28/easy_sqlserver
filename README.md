# Easy SQLSERVER

This is a simple library to assist in manipulating SQL Server data

## Requirements

* Python >= 3.5
* Set the environments (Eg: **export SQLSERVER_SERVER=0.0.0.0**)
  * SQLSERVER_SERVER
  * SQLSERVER_PORT
  * SQLSERVER_USERNAME
  * SQLSERVER_PASSWD
  * SQLSERVER_DATABASE

## Installing
```
pip install easy-sqlserver
```

## How can I use?

### Methods

 * limit(int): Sets the number of records retrieved (By default it's 1000)
 * where(str or list): Sets conditions on where clause
 * select(str): Set the table
 * join(str, str): Set the join table in first parameter and condition in second parameter
 * fields(list): Set list of fields to show (By default it's all (*))
 * query(str): If you want write a query to execute, use this method
 * order_by(str): If you want ordering results, use this method

* **Example 1**
```
from easy_sqlserver import EasySQLServer


easy_sqlserver = EasySQLServer()
easy_sqlserver.select("MY_TABLE1")
easy_sqlserver.join("MY_TABLE2", "MY_TABLE1.id = MY_TABLE2.my_table1_id")
easy_sqlserver.where("MY_TABLE1.id = 11")
results = easy_sqlserver.execute()
```
* **Example 2**
```
from easy_sqlserver import EasySQLServer


easy_sqlserver = EasySQLServer()
easy_sqlserver.select("MY_TABLE1")
easy_sqlserver.join("MY_TABLE2", "MY_TABLE1.id = MY_TABLE2.my_table1_id")
easy_sqlserver.where(["MY_TABLE1.name like '%jose%'", "MY_TABLE1.type=2"])
results = easy_sqlserver.execute()
```

* **Example 3**
```
from easy_sqlserver import EasySQLServer


easy_sqlserver = EasySQLServer()
easy_sqlserver.query("SELECT TOP 10 FROM MY_TABLE1")
results = easy_sqlserver.execute()
```