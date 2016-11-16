# -*- coding: utf-8 -*-

import pymysql

config = {
   'user': 'root',
   'password': '123456',
   'host': 'localhost',
   'database': 'database_test',
   'table': 'table_test',
   'raise_on_warnings': True,
   'unix_socket': '/var/run/mysqld/mysqld.sock'
}

data_file = 'mysql-test.dat'

create_database_test = "CREATE DATABASE IF NOT EXISTS " + config.get('database')

use_db = "use " + config.get('database')

create_table_sql = "CREATE TABLE IF NOT EXISTS " + config.get('table') + " ( \
                   FIRST_NAME  CHAR(20) NOT NULL, \
                   LAST_NAME  CHAR(20), \
                   AGE INT, \
                   SEX CHAR(1), \
                   INCOME FLOAT )"

inset_table_item = "INSERT INTO " + config.get('table') + " (FIRST_NAME, \
                   LAST_NAME, AGE, SEX, INCOME) \
                   VALUES ('Mac', 'Mohan', 20, 'M', 2000)"

# 打开数据库连接
db = pymysql.connect(user=config.get('user'), passwd=config.get('password'), unix_socket=config.get('unix_socket'))

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

try:
   # 创建数据库
   cursor.execute(create_database_test)

   # 选择数据库
   cursor.execute(use_db)

   # 创建数据表
   cursor.execute(create_table_sql)

   # 插入数据项
   cursor.execute(inset_table_item)

   # 提交到数据库
   db.commit()

except:
   # 如果发生错误则回滚
   print("error, to rollback")
   db.rollback()

# 关闭数据库连接
db.close()

