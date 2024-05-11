import mod1            #importing properties of mod1 module
y=200
def f2():
    print("x=",mod1.x) #Accessing property of mod1 module
    print("y=",y)
    z=mod1.x+y
    print("z=",z)
    mod1.f1()          #Accessing or calling the function of mod1 module
    print("in f2 of mod2")
f2()
print(dir())
print(dir(mod1))

#dir() function is used to know the properties of a particular module
#dir(mod1) displays the properties of mod1 module
