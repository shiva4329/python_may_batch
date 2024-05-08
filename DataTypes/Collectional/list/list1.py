# List

    # list represent in []
    # list is a mutable(changebale)
    # list follows index
    # list allows homogenous(same datatype) values and heterogeneous(diff datatypes) values
    # list allows duplicates
    # list function is -- list()




# defining list

x = []

print(x)
print(type(x))


# homogeneous

x = [10,20,30,40]

print(x)
print(len(x))
print(type(x))



# heterogeneous

x = [10,2.10,'python',True]

print(x)
print(len(x))
print(type(x))


# duplicates
x = [10,10,20,30,20]

print(x)
print(len(x))
print(type(x))


# indexing

x = [10,20,30,40]

print(x)

# extract 20
print(x[1])

# extract 20 in -ve index
print(x[-3])

# extract 20,30
print(x[1:3])

# extract 20,30 -ve index
print(x[-3:-1])



# mutable (changebale)

x = [10,20,30]

x[1] = 200

print(x)

x[2] = 300

print(x)


# mutable

# same value with diff variable == diff addresss

x = [10,20,30,40]

y = [10,20,30,40]

print(x,id(x))

print(y,id(y))


# same value with same variable == diff addresss

x = [10,20,30,40]

print(x,id(x))

x = [10,20,30,40]

print(x,id(x))


# diff value with same variable == diff addresss

x = [10,20,30,40]

print(x,id(x))

x = [10,20,300,40]

print(x,id(x))




# # memory address validation


# # diff variable with same value --> same address


# x = 10

# y = 10

# print(x,y)

# # print(x)

# print(id(x))
# print(id(y))


# # diff variable with diff value --> diff address


# x = 10

# y = 11

# print(x,y)

# # print(x)

# print(id(x))
# print(id(y))




# # same variable with diff value --> diff address


# x = 10

# print(x,id(x))

# x = 11

# print(x,id(x))


