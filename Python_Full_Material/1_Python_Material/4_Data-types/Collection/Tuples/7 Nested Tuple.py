#Nested Tuples: tuples within a tuple

x=((10,20,30),(40,50,60),(70,80,90))

print(x,id(x))

print(len(x))

#printing each element of a tuple

print(x[0],type(x[0]),id(x[0]))
print(x[1],type(x[1]),id(x[1]))
print(x[2],type(x[2]),id(x[2]))

print("\n")
#printing each sub-tuple using for loop

for p in x:
      print(p,type(p),id(p))

#Printing each element of each sub tuple

for p in x:
    for q in p:
        print(q,type(q),id(q))
                                    
