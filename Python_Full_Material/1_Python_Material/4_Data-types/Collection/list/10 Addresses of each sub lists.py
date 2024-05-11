
x=[[10,20,30],[40,50,60],[70,80,90]]

print(x,id(x))

for p in x:
   print(p,type(p),id(p))

for p in x:
    for q in p:
        print(q,type(q),id(q))

x[0][0]=15
x[0][1]=25
x[0][2]=35

x[1][0]=45
x[1][1]=55
x[1][2]=65

x[2][0]=75
x[2][1]=85
x[2][2]=95

print("\n\n")

for p in x:
   print(p,type(p),id(p))

print("\n")
for p in x:
    for q in p:
        print(q,type(q),id(q))
