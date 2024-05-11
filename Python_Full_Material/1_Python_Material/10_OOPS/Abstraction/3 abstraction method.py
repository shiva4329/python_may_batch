#hiding a method
class sample:
    __x=100
    def display(self):
        self.__y=200
        print("x=",sample.__x)
        print("y=",self.__y)
        self.display2()
    def display2(self):
        self.z=sample.__x+self.__y
        print("sum=",self.z)
        self.__display3()
    def __display3(self):
        print("z=",self.z)
s1=sample()
s1.display()
s1.display2()
#s1.__display3()
#print(sample.__x)
#print(s1.__y)
print(s1.z)



