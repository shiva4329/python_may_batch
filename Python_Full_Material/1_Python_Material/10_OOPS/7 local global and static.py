#working with static,local and global variables
r=30     #global variable
class demo:
    x=10  #static variable
    y=20  #static variable
    print(x)
    print(y)
    def compute(self,p,q):
        z=p+q+r          #p,q,z are local variables, here sum of local and global variables.
        w=demo.x+demo.y  #sum of static variables
        print("z=",z)
        print("w=",w)
#end of the class
d1=demo()
d1.compute(40,50)
print(r) #global variables
#print(p,q,z,w)  #local variables
print(demo.x,demo.y)
