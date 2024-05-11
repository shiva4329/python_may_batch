
'''
Comprehensions:

1.List Comprehension
2.Tuple Comprehension-------->not Supported
3.Set Comprehension
4.Dictionary Comprehension

'''
# List Comprehension: Creating Lists from other Iterable types

#case 1: Creating a list from a range() function

#ex:1
x=range(10)
y=[p for p in x]
print(y,type(y))

#ex:2 generating values from 10 to 20
y=[p for p in range(10,20)]
print(y,type(y))

#ex: I want only even values
y=[p for p in range(0,20,2)]
print(y,type(y))

#ex:4 even we can specify conditions and get even values
y=[p for p in range(1,20) if(p%2==0)]
print(y,type(y))

#case 2: Creating a list from a string
x="Python is simple"
print(x,type(x))

y=x.split(" ")
print(y,type(y))

#ex:2
y=[p for p in x.split(" ")]
print(y,type(y))

#ex3:
y=[p for p in "Hello world".split(" ")]
print(y,type(y))

#ex:4
y=[p for p in "python"]
print(y,type(y))

#case 3: Creating a list from a list
#ex:1
y=[p for p in [10,20,30,40,50]]
print(y,type(y))

#ex:2:
cities=["pune","mumbai","chennai","delhi"]

#create a list from this list in which all the cities 1st character should be in uppercase
y=[p.capitalize() for p in cities]
print(y,type(y))


#ex:3 Creating nested lists
emps=["miller","Blake","James","John"]

#create a nested list from this

y=[[p,p.upper(),len(p)] for p in emps]
print(y,type(y))

#case 4 : Creating a list from a tuple
x=((101,"Miller",30000),(102,"Blake",40000),(103,"James",50000))
y=[p for p in x]
print(y,type(y),len(y))

#case 5: Creating a list from a set

y=[p for p in {10,20,30,40,50}]
print(y,type(y))










































