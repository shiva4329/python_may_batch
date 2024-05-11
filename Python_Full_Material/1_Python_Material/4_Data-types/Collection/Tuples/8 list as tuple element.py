#case 1: list as tuple element

x=((10,20,30),(40,50,60),[70,80,90])
print(x,id(x))
#x[1][1]=55

x[2][1]=85
x[2][2]="hello"
print(x,id(x))

#x[2]="python"  #error bcoz it is tuple element , cannot be modified



