# set functions and methods


# set functions 
x = {10,20,30}

print(len(x))
print(type(x))
print(id(x))

print(sorted(x))

# print(reversed(x)) # it will not work


del x

# print(x)



# methods ------

x = {10,20,30}

print(x)

# add() # adds the value in set

x.add(40)

print(x)


# clear() -- removes all elements in the set

x = {10,20,30}

x.clear()

print(x)


# pop() -- remove element random

x = {10,20,30}

x.pop()

print(x)

# remove() -- removes particular value

x = {10,20,30}
x.remove(30)
print(x)


# copy() --- compyes the data into another variable

x = {10,20,30,40}

print(x)

y = x.copy()

print(y)



#unioin() --- returns the all elements without duplicates

x = {10,20,30}

y = {20,30,40,50}

print(x.union(y))


#intersection() --- returns the common elements

x = {10,20,30}

y = {20,30,40,50}

print(x.intersection(y))


# update() - updates the set with updatates values

x = {10,20,30}

x.update({50,60})

print(x)


# difference

x = {'a','b','c'}

y = {'b','c','d'}

print(x.difference(y)) # removes y's elements from x

print(y.difference(x)) # removes x elements from y

