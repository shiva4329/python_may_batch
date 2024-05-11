#Accepting set of values from the user keyboard

print("Enter marks of 5 subjects:")

y={int(p) for p in input().split(" ")} #here generator object is created, typecast to tuple
print(y,type(y))
