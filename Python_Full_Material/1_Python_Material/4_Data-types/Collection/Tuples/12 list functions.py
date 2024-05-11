#Functions applied on a tuple

x=(30,20,10,50,40)

print(x)

print(type(x))

print(id(x))

print(len(x))

print(sum(x))

print(max(x))

print(min(x))

avg=sum(x)/len(x)

print("AVG=",avg)

print(sorted(x))  #always sorted() function returns list type

print(reversed(x))  #here elements will be reversed and are stored in another object
                    #that object address is returned.
#but to get one by one element from the reversed object use for loop
for p in reversed(x):
    print(p,end=" ")

print("\n")
for p in reversed(sorted(x)):
    print(p,end=" ")














