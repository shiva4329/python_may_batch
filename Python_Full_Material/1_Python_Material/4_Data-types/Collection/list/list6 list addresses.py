#working with list addresses

x=[10,20,30,40,50]

y=[10,20,30,40,50]

print(x,type(x),id(x))

print(y,type(y),id(y))

print(x is y)
print(x==y)

print(x[0],type(x[0]),id(x[0]))
print(y[0],type(y[0]),id(y[0]))

print(x[0] is y[0])
print(x[0]==y[0])

p=10

print(p is x[0] and x[0] is y[0])
