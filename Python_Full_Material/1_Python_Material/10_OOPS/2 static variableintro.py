within the class we can represent data using
i.static variables
ii.non static variables



Static variables:The variables which are defined within the class and defined
 outside all the methods of a class are known as static variables.


     
 ex: class sample:
          x=10 #static variable,defined within class and outside the method
          def m1():
              print(x)
-------------------------------------------------------------------------------------------------------------------
 properties of static variable:

 1.The data which is common for all the objects,then it is recommended to
  represent by using static variables.

     ex:bank name---->SBI
        withdrawlimit-->25000
    
    data which is changing from one object to another object--->then
    use non-static variable
    ex:-ename,eid,designation,salary
        
 2.for static variable,only once memory is allocated.
 
 3.A static variable can be accessed by all the methods of that class and also 
   by other classes.
   
 4.A static variable always be accessed by using classname i.e from within the class or from outside the class

 ex:
 class sample:
     x=10 #Static variable
     y=20 #Static variable
     def display(self):
         print(sample.x) #Accessing static variable using class name 
         print(sample.y)
 

 diff b/w function and method
 function will be defined ouside the class
 method will be within the class

 ex:
    class sample:
        x=10 #static variable defined within class and outside methods
        def m1(): #error bcoz, we cant define functions within class,to make
            print("Hello...........") #function as method,make it self as

        def m1(self):
            print("Hello............")












 

 
 
