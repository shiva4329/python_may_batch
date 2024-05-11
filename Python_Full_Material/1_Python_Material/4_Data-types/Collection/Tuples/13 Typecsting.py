#Type casting

#case 1: converting a list to tuple

x=[10,20,30,40,50]
print(x,type(x))

y=tuple(x)
print(y,type(y))

print("\n")

#case 2: Converting a tuple to list
a=(10,20,30,40,50)
print(a,type(a))

b=list(a)
print(b,type(b))

print("\n")

#Case 3: converting a string to list
p="python"
print(p,type(p))

q=list(p)
print(q,type(q))

print("\n")

#Case 4: converting a string to tuple
p="python"
print(p,type(p))

q=tuple(p)
print(q,type(q))

#case 5: Converting a int to list
x=10
print(x,type(x))

'''
y=list(x)
print(y,type(y))'''


y=[x]
print(y,type(y))

x1=10 ; x2=20 ; x3=30
y=[x1,x2,x3]
print(y,type(y),len(y))










