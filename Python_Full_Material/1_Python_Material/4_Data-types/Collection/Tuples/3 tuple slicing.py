#tuple slicing : Extracting particular elements from a tuple

x=(10,20,30,40,50)

print(x[0:4:3])

print(x)

print(x[1])

print(x[-2])


#extract---->10,20,30
print(x[0:3]) #upper bound excluded

#extract----->20,30,40
print(x[1:4])

print(x[4:1]) #empty tuple----->always lower to upper bound.

#extract------>20,30,40 using -ve index
print(x[-4:-1])

#extract------>30,40,50
print(x[2:5])

print(x[2: ])

print(x[ :3])

print(x[ : ])

print(x)

print(x[1:-2])
