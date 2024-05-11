#creating a BOOKS table in the DIGITALNEST
import pymysql
con=pymysql.connect("localhost","root","43294329","DigitalNest")
cur1=con.cursor()
print("-----Table Creation-----")
#cur1.execute("create table Books(sno int(2),bname char(5), author char(10), price int(4),year int(4))")
print("Table Created")
print("-----Inserting Values------")
cur1.execute("insert into Books values(1,'xyz','charan',780,1994),(2,'abc','arjun',650,1849),(3,'lmn','ram',250,1998),(4,'asd','vikram',550,1993),(5,'wings','pavan',444,1852),(6,'rooky','cruise',325,1779)")
con.commit()
cur1.execute("select * from Books")
for i in cur1:
    print(i)
print("-----Getting Selected Values------")
cur1.execute("select bname,price,year from Books")
for s in cur1:
    print (s)
