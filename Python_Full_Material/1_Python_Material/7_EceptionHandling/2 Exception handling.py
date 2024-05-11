
Exception Handling:The process of identifying raised exception object and
                    handling it by assigning that exception to corresponding
                    run-time error representation class is known as
                    Exception handling.

we can implement exception handling using try & except block.

we need to follow indentation for both try and except blocks.


1)try block:
syntax:

try:
    .......
    .......
    .......
    ....... for identifying raised exception
    The Stmts which causes run-time errors are placed within try block.


ex:
    
x=int(input("enter x value"))
y=int(input("enter y value"))
try:
    z=x/y
    print(z)


If exception is raised in 1st stmt of try block,then control will go to
except block,without executing the remaining stmts of try block.


except block syntax:

except(Exception class name):
    ........................
    .......................
    .......................
    .......................

except block assigns the exception object to the corresponding run-time error
representation class.
we can also display user-friendly error messages in except block.

ex:
except(ZeroDivisionError):#assigning exception object to corresponding run-time error representation class
    print("2nd No cannot be Zero")#we can display user-friendly error message.



    
    
