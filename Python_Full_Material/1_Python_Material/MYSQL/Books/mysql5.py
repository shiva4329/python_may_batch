#updating and deleting in Books
from mysql4 import *
cur1.execute("update Books set price=price+50 where sno>4")
con.commit()
print("++++ UPDTED Price++++")
cur1.execute("select bname,price from Books")
for r in cur1:
    print (r)
cur1.execute("delete from Books where sno=3")
print("---------DELETED Books-----------")
cur1.execute("select * from Books")
for x in cur1:
    print(x)
cur1.close()
con.close()
