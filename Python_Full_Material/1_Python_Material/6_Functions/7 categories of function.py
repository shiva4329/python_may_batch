

#categories of function: 4 categories

#1)Function without parameters and without returntype

def add1():
    x=10
    y=20
    z=x+y
    print("sum=",z)
add1()

#2)Function with parameters and without returntype

def add2(x,y):
    z=x+y
    print("sum=",z)
    
print(add2(30,40))

#Note: functions can also be used for assignments

#3)Functions with parameters and with returntype.

def add3(x,y):
    z=x+y
    print(z)
    return z
p=add3(50,60)
print("sum=",p)

#(or)
print(add3(50,60))

#4) Functions without parameters and with returntype

def add4():
    x=10
    y=20
    z=x+y
    return z

q=add4()
print("sum=",q)

print(p+q)


#ex: A function can return multiple values

def compute(s1,s2,s3):
    tot=s1+s2+s3
    avg=tot/3
    return tot,avg
m,n=compute(90,80,70)
print("Total=",m)
print("Average=",n)









