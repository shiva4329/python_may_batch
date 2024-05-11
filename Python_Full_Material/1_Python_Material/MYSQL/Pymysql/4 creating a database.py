

#Creating,inserting and retrieving data from a database by writing python scripts

import pymysql

con=pymysql.connect('localhost','root','root')
#here con is a connection object which is created automatically whenever we call connect()method.

#to execute any sql query,we require cursor object.

#How to create cursor object?
#if we pass cursor()method on connection object(con) then cursor object is created.

cur1=con.cursor()
cur1.execute("create database mydb5")

cur1.close()
con.close()
