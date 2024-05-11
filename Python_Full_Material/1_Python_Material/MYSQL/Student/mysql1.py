# cretaing student table in Database
import pymysql
con=pymysql.connect("localhost","root","43294329","DigitalNest")
cur1=con.cursor()
#cur1.execute("create table student(sname char(10),sroll int(3),sbranch char(10),smarks int(5),sclg char(10))")
cur1.execute("insert into student values('a',1,'ECE',150,'KLU'),('b',2,'CSE',200,'NIET'),('c',3,'EEE',210,'VIT')")
con.commit()
cur1.execute("select * from student")
for i in cur1:
    print(i)
cur1.execute("select sname,sclg from student")
for p in cur1:
    print (p)
#cur1.close()
#con.close()
