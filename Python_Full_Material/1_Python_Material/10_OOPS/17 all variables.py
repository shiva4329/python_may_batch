
#Program illustrating all types of variables
x=10            #global variable
class test:
    y=20        #static variable
    def display(self,p):
        self.z=p      
        self.w=x+test.y+self.z+p
        print("x=",x)  #printing global variable
        print("p=",p)  #printing local variable
        print("y=",test.y) #printing static variable
        print("z=",self.z) #printing non-static variable
        print("w=",self.w) #printing non-static variable
#end of the class
t1=test()
t1.display(30)
print(x)
print(test.y)
print(t1.z)
print(t1.w)
#print(p)  # local variable cant be accessed 

