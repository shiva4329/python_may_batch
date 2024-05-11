#case 2: Tuple as list element

x=[[10,20,30],[40,50,60],(70,80,90)]

print(x,id(x))

for p in x:
    print(p,type(p),id(p))

#x[2][1]=85
x[1][1]=55

print("\n")

x[0]=4.3
x[1]=True
x[2]="python"

print(x,id(x))

for p in x:
    print(p,type(p),id(p))
