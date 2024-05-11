Exception Handling:

Generally, there are 2 types of errors in python
1.Syntax errors
2.Run-time errors

1)Syntax errors: The errors that occur due to wrong syntaxes

ex: wrong space indentation
    missing colon
ex:
def display()  #syntax error------>missing colon
print("hello") #syntax error------>wrong indentation
    

Python interpreter checks for syntax errors and then converts source code
to byte code(.pyc) and then converts this byte code to machine code.

If there are syntax errors,then .pyc file wont be generated,
If .pyc file is not generated then the python program wont be executed.


----------------------------------------------------------------------------------------------------------

2)Run-time errors:   Errors that occur at run-time,i.e during the execution of the program.

ex:Trying to access an element which is not present ------>we get Runtime Error
   Trying to remove an element which is not present------->we get Runtime error
 
ex-1: x=[10,20,30,40,50]
    trying to access 10th element---Runtime error
    print(x[10])----Runtime error

    
ex-2: Trying to remove an element which is not present-----> gives runtime error
 ex: x.remove(90)----->Runtime error

 
whenever we get run-time error,program execution is terminated abnormally

for every run time error,corresponing pre-defined python classes are availabe,
these classes are called as Exception classes.


Exceptions are the classes,which contain run-time error representations.

when ever we get run-time error,run-time error representation class object
will be created automatically
whenever this object is created,we say that exception is raised, we need to
handle it with a code,otherwise abnormal termination.





Abnormal Termination: Termination of program in middle of execution without executing
last stmt

2 types of exceptions:
    
Pre-defined Exceptions------>Raised automatically and we need to handle
User-defined Exceptions----->We need to raise and we need to handle


reasons for run-time errors:
1.Entering invalid input
2.Due to invalid code
3.memory related issues
4.Hardware related problems.





















