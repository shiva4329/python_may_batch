
#Single Inheritence: A derived class with a  single base class

class A:
    def m1(self):
        print("from m1......")
a1=A()
a1.m1()
print(A.__bases__)


#here A is a derived class with a single base class(object class)
