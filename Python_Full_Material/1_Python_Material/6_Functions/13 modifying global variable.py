#modifying global variable value within the function

x=10
y=20
def display():
    global x  #forward declaration , this declaration says that u r going to modify global variable
              #in the later stmt
    
    x=15
    print(x)
    print(y)


def show():
    print(x)

show()
display()
show()
