# tuple function and methods

x = (10,20,30,40)

print(len(x))

print(type(x))

print(id(x))


# sorted() - returns the data in ascending order in  list type

x = (10,30,20,50,40)

print(sorted(x))


# reversed() --- reverses the tuple but it returns indirect address of the reversed tuple

x = (10,30,20,60,50)

print(reversed(x))



# assignment



del x

# print(x)


# below methods will not work in tuple because of tuple is immutable

# append()
# insert()
# pop()
# clear()
# remove()