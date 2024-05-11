

#Local and Global variables with same name

x=10

def display():
    x=20
    print(x)   #Always local is given preference over global

def show():
    print(x)

display()
show()
