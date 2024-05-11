#Dictinary Comprehension: Creating Dictionary from other Iterable types

#case 1:Creating dictionary from a range() function
x={p:p**2 for p in range(1,11)}
print(x,type(x))

#ex:2
x={p:p+1 for p in range(1,11)}
print(x,type(x))

#case 2: Creating a dictionary from a string

x="Python is simple"
y={p:len(p) for p in x.split(" ")}
print(y,type(y))

#case 3: Creating a dictionary from a list
x=["Miller","John","Blake","James"]

y={p:len(p) for p in x}

#case 4: Creating a dictionary from a Tuple
x=("Miller","John","Blake","James")

y={p:len(p) for p in x}
print(y,type(y))
#case 5: Creating a dictionary from a set
x={"Miller","John","Blake","James"}

y={p:len(p) for p in x}
print(y,type(y))
