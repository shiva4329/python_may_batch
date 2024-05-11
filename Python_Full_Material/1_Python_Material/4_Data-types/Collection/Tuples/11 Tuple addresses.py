#working with tuple addresses
#list
a=[1,2,3,4,5]

b=[1,2,3,4,5]

print(a,id(a))

print(b,id(b))

print(a is b)

print(a == b)


#tuple
x=(1,2,3,4,5)

y=(1,2,3,4,5)

print(x,id(x))

print(y,id(y))

print(x is y)

print(x == y)


print(a[0],type(a[0]),id(a[0]))
print(b[0],type(b[0]),id(b[0]))    
print(a[0] is b[0])

print(x[0],type(x[0]),id(x[0]))
print(x[0] is a[0])

p=1

print(x[0] is p)


c=((10,20,30),(40,50,60),[70,80,90])
d=((10,20,30),(40,50,60),[70,80,90])
print(c,type(c),id(c))
print(d,type(d),id(d))

print(c is d)


      
