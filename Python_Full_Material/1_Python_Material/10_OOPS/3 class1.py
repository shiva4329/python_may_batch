class sample:
    '''sample class'''
    x=10 #static  variable
    y=20 #static variable
    def display(self):   #always a method should have self as a parameter
        print("x=",sample.x)
        print("y=",sample.y)
        print(self)
    #end of the class

#how to create objects?
#objname=classname()      #syntax for cereating object
s1=sample()  #object creation stmt ,an object is created internally and it address is stored in a
             # variable called as reference variable(s1)
print(s1)    #prints the address of the object.
#by using this object(ref variable) we can access the class members
s1.display() #display method will be executed and the address of s1 will be stored in self of display

print(sample.x)#accessing static variable from outside the class
print(sample.y)


#creating one more object
s2=sample()
print(s2)
s2.display() #here s2 address will be stored in self of display()
    
    
