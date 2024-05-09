# Tuple

    # tuple represent in ()
    # tuple is a im-mutable(un-changebale)
    # tuple follows index
    # tuple allows homogenous(same datatype) values and heterogeneous(diff datatypes) values
    # tuple allows duplicates
    # tuple function is -- tuple()



# tuple defining
x = ()

print(x,type(x))



x = 10,20,30
print(x,type(x))



# duplicates

x = (10,20,10,20,30) 

print(x)

# heterogenous

x = (10,20.3,'python',True)

print(x)


# index

x = (10,20,30,40,50)

print(x[1:3])

print(x[3])


# im-mutable


x = (10,20,30,40,50)

# x[1] = 200 # error bcoz of immutable

print(x)


# same values with diff variable == same address

x = (10,20,30)

print(id(x))

y = (10,20,30)

print(id(y))


# dif values with same variable == diff address

x = (10,20,30,40)

print(id(x))

x = (10,20,30)

print(id(x))



# same values with same variable == same address

x = (10,20,30,40)

print(id(x))

x = (10,20,30,40)

print(id(x))

