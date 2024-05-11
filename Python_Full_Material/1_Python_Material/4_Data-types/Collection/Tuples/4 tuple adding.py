#merging 2 tuples
x=(10,20,30)
y=(40,50,60)
z=x+y
print(z)


y=(10,20,30,40,50,60)
z=y[0:2] + y[4: ]
print(z)
