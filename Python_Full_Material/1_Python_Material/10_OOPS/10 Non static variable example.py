#Program illustrating static and NSV
x=30
print(x,id(x))
class sample:
    a=10 #sv
    b=20
    def display(self):
        self.x=30
        self.y=40
        print(sample.a)
        print(sample.b)
        print(self.x) #Accessing NSV  within the class using self
        print(self.y)
        print(self)
#end of the class

s1=sample() #object creation stmt 
print(s1)
#s1.display()
print(s1.x) #Accessing NSV from outside the class
print(s1.y)

print(id(s1.x),id(s1.y))
s1.x=35
s1.y=45
print(id(s1.x),id(s1.y))


s2=sample()
print(s2)
s2.display()
print(s2.x)
print(s2.y)
print(id(s2.x),id(s2.y))
print(type(s2.x),type(s2.y))













