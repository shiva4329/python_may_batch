# update a customer bal and delete a customer
'''from mysql2 import *
cur2=cur1
cur2.execute("select * from customer")
print("--updated values--")
cur2.execute("update customer set bal=bal+500 where cid=12")
con.commit()
cur2.execute("select cname,bal from customer")
cur2.close()
con.close()'''
import pymysql
con=pymysql.connect('localhost','root','43294329','DigitalNest')
cur1=con.cursor()
print("---updated balance----")
cur1.execute("update customer set bal=bal+520 where cid=13")
con.commit()
'''cur1.execute("select* from customer")
for i in cur1:
    print(i)'''
cur1.execute("select cname,bal from customer")# for selected elements
for p in cur1:
    print (p)
print("--deleted customer--")
cur1.execute("delete from customer where cname='Samba'")
cur1.execute("select * from customer")
for r in cur1:
    print(r)
cur1.close()
con.close()

