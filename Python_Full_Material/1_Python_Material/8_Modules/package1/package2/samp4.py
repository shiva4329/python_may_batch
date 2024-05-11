import demo.test.samp1 as s1
import demo.test.samp2 as s2
import demo.samp3 as s3
import math

w=s1.x+s2.y+s3.z

def display4():
    s1.display1()
    s2.display2()
    s3.display3()
    print("w=",w)
    print("pi=",math.pi)
    print("sqrt=",math.sqrt(16))
display4()
