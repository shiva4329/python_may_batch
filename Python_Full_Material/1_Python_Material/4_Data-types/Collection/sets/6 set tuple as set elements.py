#tuples as set elemnts
x={(10,20,30),(40,50,60),(70,80,90)} #only immutable elements are allowed within set
print(x)
print(type(x))
print(len(x))

for p in x:         #printing each tuple
    print(p,type(p))

    
for p in x:         #printing elements of each tuple
    for q in p:
        print(q,type(q))

#x={[10,20,30],[40,50,60],[70,80,90]}  #we cant have list as set elements
                                       #as they r mutable
#print(x)
