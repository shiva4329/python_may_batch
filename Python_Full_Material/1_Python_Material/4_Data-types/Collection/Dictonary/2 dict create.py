# creating dictionary elements

x={"sachin":90,"Ganguly":65,"Dravid":35}  # homogeneous keys(string type),homogeneous values(int type)
print(x)
print(type(x))
print(len(x))


y={"height":5.5,1:"male",2.99:3} #heterogeneous keys and heterogeneous values
print(y)
print(type(y))
print(len(y))


z={"CSE":120,"ECE":90,"IT":60,"EEE":60,"CSE":60} #duplicate keys are not allowed,but values are allowed.
print(z)
print(type(z))
print(len(z))


x={"a":20,"b":5,"a":10,"b":15,"a":3}
print(x,len(x))

p={"x":100,"y":200,"y":400,"x":300}
print(p)



a={ } 
print(a)
print(type(a))
print(len(a))


a={10,20}
print(a,type(a))

y={"a":10,"b":20}
print(y,type(y))

b=dict() #empty dictionary
print(b)
print(type(b))
print(len(b))

d={"rank":15}
print(d)
c=dict(d) #what parameters we can pass in dict function---->passing dictionary as a parameter
print(c)
#or

e=d  #assigning one dictionary to another dictionary.
print(e)
print(d)
print(type(e))
print(len(e))


x=int("10")
print(x,type(x))

'''
y=int("hello")  
print(y)
'''

'''
p=dict([10,20,30,40,50])
print(p,type(y)) 
'''

p=dict([("kohli",30),("Dhoni",36),("Rohith",32)])
print(p,type(p))

p=dict([["kohli",30],["Dhoni",36],["Rohith",32]])
print(p,type(p))

p=dict((["kohli",30],["Dhoni",36],["Rohith",32]))
print(p,type(p))

p=dict([{"kohli",30},{"Dhoni",36},{"Rohith",32}]) #valid but not recommended
print(p,type(p))


#In a dictionary, value can be of any type like int,float,string,bool.list,tuple,set,dictionary

x={"emps":["John","Miller","Rahul","Ajay"]}
print(x,len(x))
print(x["emps"])    #If u pass the key , u will get the value
print(type(x["emps"]))







