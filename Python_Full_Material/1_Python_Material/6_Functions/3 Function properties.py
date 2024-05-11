#Function properties

#1. A function can be called for multiple times.

def display():      #Function definition
    '''function to print a msg'''
    print("Good Morning....")

display()           #function call
display()
display()

#Advantage : re-usability

#2.The order in which the functions are called and the order in which they are defined
# need not be the same.

def English():
    print("ABCDEFGHIJK.......")

def maths():
    print("123456789......")

def chemistry():
    print("H2o is the chemical name of water..")



maths()
English()
chemistry()
maths()

#----------------------------------------------------------------------------------------------------
#3.one function can call another function

def display():
    print("hello")
    show()

def show():
    print("Good Morning...")
display()


#---------------------------------------------------------------------------------------------------
#4. Defining a function in another function

def compute():
    print("hello")
    def disp():
        print("hai...")
    disp()

compute()





















