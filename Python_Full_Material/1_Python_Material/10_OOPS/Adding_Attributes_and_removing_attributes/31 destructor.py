#Destructor: whenever a object gets removed destructor will be executed
#Destructor is defined by using the name __del__
#Destructor will be executed automatically whever a object gets removed
class test:
    def __init__(self):            #Constructor
        print("constructor called")
    def __del__(self):             #Destructor
        print("destructor called")
    
t1=test() #RC=1
t2=test() #RC=1
t3=test() #RC=1
print(t3)
#t4=t3
t3=test() #If same ref variable is used,then RC decreases by 1
          #RC=0(if same variable is used,RC becomes less i.e 0
          #previous t3 object is removed ,Destructor executed.
          #and a new t3 object is created.
print(t3)





