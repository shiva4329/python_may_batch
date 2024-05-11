

#Creating a table ,inserting data and retrieving data from a database by writing python script.

import pymysql

con=pymysql.connect('localhost','root','root','mydb5')#con is connection object

cur1=con.cursor() #cur1 is cursor object

#cur1.execute("create table emp(eid int,ename varchar(10),sal int,sex  char(1),dno int,city varchar(10))")

cur1.execute("insert into emp values(101,'Miller',10000,'m',11,'hyd'),(102,'Blake',20000,'m',12,'pune'),(103,'Sony',30000,'f',11,'hyd'),(104,'Sita',40000,'f',12,'pune'),(105,'John',50000,'m',13,'hyd')")
con.commit()  #making the changes permanent, i.e permanently saved
cur1.execute("select * from emp")

for p in cur1:
    print(p)

cur1.close()
con.close()


