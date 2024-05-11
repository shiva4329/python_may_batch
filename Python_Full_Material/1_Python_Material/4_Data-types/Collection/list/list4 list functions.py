#Functions applied on a list

x=[30,20,10,50,40]

print(x)

print(type(x))

print(id(x))

print(len(x))

print(sum(x))

print(max(x))

print(min(x))

print(sorted(x))

print(reversed(x)) #reverses the elements and stores in another object and that object address
                   # will be returned.

#To get one by one element from reversed object, apply for loop

for p in reversed(x):
    print(p,end=" ")

print("\n")
for p in reversed(sorted(x)):
    print(p,end=" ")


