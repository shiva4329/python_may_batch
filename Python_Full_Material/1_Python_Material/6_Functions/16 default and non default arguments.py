#combination of non-default and default

def display(name,city="hyd"):
    print(name,city)

#display()
display("Peter")
display("kumar","pune")

#combination of default and non-default

def show(name="Miller",city):
    print(name,city)

show("Blake","pune")
show("mumbai")

#Note :we cannot define non-default arguments after default arguments

