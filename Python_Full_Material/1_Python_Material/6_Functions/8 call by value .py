#call-by-value: calling a function by providing some values

def compute(x,y):
    z=x+y
    print("z=",z)

compute(10,20)  #Call-by-value

#call-by-reference : Calling a function by providing some reference

def show(x,y):
    z=x+y
    print("z=",z)

a=10
b=20
show(a,b)
