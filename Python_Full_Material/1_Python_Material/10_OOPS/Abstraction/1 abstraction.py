#Abstraction: The concept of hiding the properties of one class from other classes or
#outside classes is known as Abstraction.
#ex: S.v can be accessed from outside the class using classname,but i want to restrict this
#In order to hide the properties of a class, we use __ at the beginning of the property name
#ex: __x=10

class sample:
    __x=100
    x=10
    def display(self):
        print(sample.__x,type(sample.__x))
        print(sample.x,type(sample.x))
s1=sample()
s1.display()
#print(sample.__x)  #cant be accessed from outside the class
print(sample.x)
