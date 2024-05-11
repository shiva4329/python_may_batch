
'''
import demo.test.samp1 as s1
import demo.test.samp2 as s2
import demo.samp3 as s3
import math
'''
from demo.test import samp1 as s1 #If 2 modules have same varible name then we can go for aliasing
from demo.test.samp2 import *     #within from import
from demo.samp3 import *
from math import *





w=s1.x+y+z

def display4():
    s1.display1()
    display2()
    display3()
    print("w=",w)
    print("pi=",pi)
    print("sqrt=",sqrt(16))
display4()

















