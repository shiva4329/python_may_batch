#Renaming a module:
#if the module name is big,we can use alias names to access the properties

import studentmarks1 as s
total=s.maths+s.phy+s.chem
avg=total/3
def show():
    s.display()
    print("total:",total)
    print("Avg:",avg)
show()
