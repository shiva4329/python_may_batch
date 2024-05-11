#Set Comprehension : Creating Set from other Iterable types

#Case 1: Creating set from range() function

x={p for p in range(1,11) }
print(x,type(x))


#case 2:Creating set from string
x="Good Morning Hyderabad"
y={ p for p in x.split(" ")}
print(y,type(y))

#case 3: Creating set from a list
x=[10,20,30,40,50,10,20,30]
y={p for p in x}
print(y,type(y))

#Case 4: Creating set from tuple

x={p for p in (10,20,30,40,50)}
print(x,type(x))

#case 5: Creating a set from a set

x={p for p in {10,20,30,40,50}}
print(x,type(x))

