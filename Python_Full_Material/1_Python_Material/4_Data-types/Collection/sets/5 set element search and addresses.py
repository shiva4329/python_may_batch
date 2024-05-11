#searching for an element in set
x={10,20,30,40,50}
print(x,id(x))

print(20 in x)
print(70 in x)
print(70 not in x)

#working with set addresses

y={10,20,30,40,50}
print(y,id(y))
print(x is y)  
print(x==y)    

x={10,20,30,40,60}
print(x,id(x))
print(x is x)
print(x==x)



a={1,2,3,4,5}
print(a)

b={1,2,3,4,5}
print(b)
print(a is b)
print(a==b)


m=10
print(m,type(m))

p=100,200,300
print(p,type(p))

a,b,c,d,e=x
print(a,b,c,d,e)


m=[10,20,30,40,50]
x1,x2,x3,x4,x5=m
print(x1,x2,x3,x4,x5)

s1,s2,s3,s4,s5=[100,90.50,75,80,92]
print(s1,s2,s3,s4,s5)
print(s1,type(s1))
print(s2,type(s2))


x1,x2,x3,x4,x5=range(5)
print(x1,x2,x3,x4,x5)






