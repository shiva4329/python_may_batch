#creating set object
x={10,20,30,40,50}  #homogeneous elements
print(x)
print(type(x))
print(len(x))

y={501,6.1,True,"hello"} #heterogeneous elements
print(y)
print(type(y))
 
z={10,20,30,(30,40,50,60)}  # only immutable elements are allowed within set
print(z)
print(type(z))
print(len(z))

a=set()           #creating empty set
print(a)
print(type(a))
print(len(a))

b=set("hello")    #creating set with data
print(b)          #only one parameter allowed witin a set()
print(type(b))    #i.e string or iterable types like list,tuple,set etc
print(len(b))

m=set([10,20,30,40,10])    
print(m)          
print(type(m))  
print(len(m))

n=set({10,20,30,40})    
print(n)          
print(type(n))  
print(len(n))

'''
m=set(10)    
print(m)          
print(type(m))  
print(len(m))'''

#--------------------------------------------------------
#diff b/w---->set((1,2,3,4)) and {(1,2,3,4)}

a={(1,2,3,4,5)}
print(a)
print(len(a))

b=set((1,2,3,4,5))
print(b)
print(len(b))

c=set([(1,2,3),(4,5,6)]) 
print(c)
print(len(c))

'''
d=set(([1,2,3],[4,5,6])) 
print(d)
print(len(d)) '''
#---------------------------------------------------------
c={10,20,10,20,30} #duplicate elements will be eliminated
print(c)
print(len(c))

'''d={{10,20,30},{40,50,60},{70,80,90}} # sets within set are not allowed
print(d)'''
