def display(x,y,*z):
    print("x=",x,type(x))
    print("y=",y,type(y))
    print("z=",z,type(z))
    
display(10,20,30)
print("\n")
display(10,20,30,40,50)
print("\n")
display(10,20)
print("\n")
display(10,20,"hello")
print("\n")
display(10,"hai","hello")
print("\n")
display(10,"hai","hello","world")
print("\n")
display(10,20,30,[40,50])


