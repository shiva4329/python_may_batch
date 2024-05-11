''' there are 2 types of imports
1.Normal import
2.From import
1.Normal import:Here to access the properties of imported module,
everytime we need to use the module name before the property name.
 ex:  mod1.x--->accessing variable of mod1
 ex: mod1.f1()--->accessing function of mod1



From import:whenever we import a module,by using "from" import,then
we can access the properties of that module directly without using the module name
using from imort, we can import particular property or properties  '''

from mod1 import x,f1     #importing particular property
from math import pi,e
y=200
def f2():
    print("in f2 function")
    print("x=",x)  #without module name importing x
    f1()           #accesing function f1 of mod1 directly
    print("y=",y)
    z=x+y
    print("sum=",z)
    print("pi=",pi)
    print("e=",e)
f2()

