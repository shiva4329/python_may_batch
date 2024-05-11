#Anonymous function/Lambda function:

 #A function which doesnt have any name,is called lambda fn or Anonymous function

    #syntax: lambda arguments:expression
   
# how to call lambda function?
# Ans: Assign lambda function to a variable,this variable behaves like fn name
        #using that variable name,we can call lambda fn.

#ex: function to square a no
f1=lambda x:x*x
print(type(f1))
p=f1(10)
print(p)
q=f1(20)
print(q) 

#The above code is equivalent to the following code
def f2(x):
    return(x*x)
p=f2(10)
print(p)
q=f2(20)
print(q)

#Lambda function can have any number of arguments but only one expression,
#which is evaluated and returned.

print("\n\n")

#ex:2
f1=lambda x,y:x*y          #Non-default arguments
p=f1(10,20)                
print(p)

print("\n\n")

#ex:3
f1=lambda x=15,y=20:x*y    #Default argumets
p=f1(10,20)                #Non keyword argumemts
print(p)
q=f1(x=20,y=30)            #keyword arguments
print(q) 
r=f1()
print(r)



