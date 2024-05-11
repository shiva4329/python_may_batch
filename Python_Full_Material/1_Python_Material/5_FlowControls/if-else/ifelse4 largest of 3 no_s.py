#Nested if-else :

#Program to find the largest of 3 numbers.

x=int(input("Enter value of x:"))
y=int(input("Enter value of y:"))
z=int(input("Enter value of z:"))

if(x>y):
    if(x>z):
        print(x,"is largest")
    else:
        print(z,"is largest")
else:
    if(y>z):
        print(y,"is largest")
    else:
        print(z,"is largest")
    

