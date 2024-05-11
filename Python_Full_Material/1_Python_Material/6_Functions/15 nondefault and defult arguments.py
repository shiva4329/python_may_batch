'''
Function arguments :4types

1)Non-default arguments or positional arguments
2)Default arguments
3)non-keyword arguments
4)Keyword arguments

1)Non-default arguments: arguments which are specified within function definition
                         and the argument values we need provide compulsorily within
                         the function call  '''

def display(name,city):  #non-default arguments
    print(name,city)

display("John","Hyd")
#display("John","chennai","pune")
#display("James")
#display()

#2)Default arguments : arguments defined within function definition with default values
#                      and it is not mandatory to provide values within the functioncall.

def show(name="James",city="pune"):
    print(name,city)


show("Ajay","Ameerpet")
show("Blake")
show()    


#Ex:1
name="George"
city="mumbai"

def show1():
    print(name,city)

show1()

    
