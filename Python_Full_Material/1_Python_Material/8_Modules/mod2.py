import mod1

y=20
z=mod1.x+y

def show():
    mod1.display()
    print("y=",y)
    print("z=",z)
show()

print(dir()) # it prints the properties of main module(mod2.py)

print(dir(mod1))

#print(),id(),len(),type(),sum(),max() etc are built-in functions present within __builtins__module

#__builtins__ is the only module in python without importing , we can use its properties

print(dir(__builtins__))
