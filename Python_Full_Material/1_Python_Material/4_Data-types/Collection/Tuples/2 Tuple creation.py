#Creating Tuples

x=(10,20,30,40,50)     #homogeneous tuple

print(x)
print(type(x))
print(id(x))


y=(501,"James",6.1,True)  #heterogeneous tuple

print(y)
print(type(y))
print(id(y))


z=100,200,300
print(z)
print(type(z))
print(id(z))

#we can also create tuple using tuple() function

x=tuple()   #empty tuple
print(x)
print(type(x))
print(len(x))


#creating tuple with content
x=tuple('python')
print(x)
print(type(x))
print(len(x))

'''
x=tuple("python","Java")   
print(x)
print(type(x))
print(len(x)) '''

#Error bcoz tuple() function accepts only one parameter and that too of iterable types like
# string,list,tuple,set etc
'''

x=tuple(10)   #error----->bcoz int is not iterable 
print(x)
print(type(x))
print(len(x))  '''

x=tuple(['python','java'])
print(x)
print(type(x))
print(len(x))

x=tuple([10,20,30,40,50])
print(x)
print(type(x))
print(len(x))


















































