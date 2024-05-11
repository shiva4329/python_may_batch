import demo.samp1 as s1
import demo.samp2 as s2

z=30

w=s1.x+s2.y+z

def display3():
    s1.display1()
    s2.display2()
    print("z=",z)
    print("w=",w)
display3()
