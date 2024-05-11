#updating and deleting student
from mysql0 import*
cur1.execute("update student set smarks=smarks+50 where sname='b'")
con.commit()
print("++++ UPDTED MARKS++++")
cur1.execute("select sname,smarks from student")
for s in cur1:
    print (s)
cur1.execute("delete from student where sroll=3")
print("---------DELETED STUDENT-----------")
cur1.execute("select * from student")
for x in cur1:
    print(x)
