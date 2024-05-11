#Special Operators: 2types
'''
1)Identity Operators
2)Membership Operators

1)Identity Operators : These operators are used to compare the addresses of 2 objects
  Identity operators are of 2 types:
      i)is
      ii)is not   '''


x=10

y=20
print(x,id(x))
print(y,id(y))

print(x is y)
print(x == y)
print(x is not y)

a=10

b=10

print(a is b)
print(a == b)


x=[10,20,30,40,50]

y=[10,20,30,40,50]
print(y,id(y))
y[2]=35

print(x,id(x))
print(y,id(y))

print(x is y)
print(x == y)
print(x is not y)

















