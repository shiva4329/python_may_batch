# list functions and methods



# list Functions


x = [10,20,30,40]

# len() -- returns length
print(len(x))

# id() -- returns address
print(id(x))

# type() -- returns type of data
print(type(x))

# sorted() --- sorts the list(ascending order)

x = [10,30,20,60,50]

print(sorted(x))

# reversed() -- reverses the list but it returns indirect address of the reversed list

x = [10,20,30,40]

print(reversed(x))

# for upacking need to use loops
for i in reversed(x):
    print(i)

# del -- deletes the entire list

del x

# print(x)






# list methods

x = [10,20,30,40]


# append() --- adds the item at the end of the list

x.append(50)

print(x)



# insert() --- inserts the item at particular position
# syntax - var.insert(index,value)

x.insert(1,15)

print(x)

# pop() --- removes the end value

x.pop()

print(x)


# pop() --- removes the index value

x.pop(1)

print(x)

# remove() --- removes the particular value

x.remove(30)

print(x)

# clear() -- removes the all items in the list returns empty list

x.clear()

print(x)