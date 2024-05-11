#hiding static and NSV

class sample:
    __x=100
    def display(self):
        self.__y=200
        print(sample.__x)
        print(self.__y)
s1=sample()
s1.display()
print(sample.__x) #S.V
print(s1.__y)  #NSV


