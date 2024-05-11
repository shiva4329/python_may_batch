#creating table ,inserting ,selecting and deleting elements in the table of DigitalNest
import pymysql
con=pymysql.connect('localhost','root','43294329','DigitalNest')
cur1=con.cursor()
#cur1.execute("create table customer(cid int,cname char(10),cacc int(10),bal int(10),cadd char(10))")
cur1.execute("insert into customer values(10,'Shiva',10001,5000,'Ongole'),(11,'Samba',10002,6000,'Vizag'),(12,'Siri',10003,7000,'Ballary'),(13,'Hari',10003,8000,'Kurnool')")
con.commit()
cur1.execute("select* from customer")
#cur1.execute("select cname,bal from customer")
for i in cur1:
    print(i)
cur1.execute("select cname,bal from customer")# for selected elements
for p in cur1:
    print (p)
cur1.close()
con.close()
