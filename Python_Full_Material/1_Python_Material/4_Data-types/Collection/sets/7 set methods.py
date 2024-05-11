# methods of set -----add(),copy(),update(),pop(),discard(),remove(),clear()
x={10,20,30,40,50}
print(x,id(x))


x.add(60)     #adding 60 to set
print(x,id(x))

#x.add(70,80) #error bcoz---> add() accepts only one parameter

x.add((70,80,90)) # accepted but (70,80,90) taken as tuple
print("after adding:")
print(x)

x.update((60,70,80)) #for adding multiple elements
print(x,id(x))

y=x.copy()  #creates a copy of x
print("another copy :") 
print(y,id(y))

x.pop()     #removes a element randomly
print(x)

x.pop()     
print(x)

x.pop()     
print(x)

x.discard(30)
print(x)

x.remove(20) #removes particular element of our choice
print(x)

'''x.remove(95) #it gives error
print(x)''' 

x.discard(95) #wont give any error
print(x)

x.clear()  #clears all set elements
print(x)
print(len(x),id(x))
print(y,id(y))

