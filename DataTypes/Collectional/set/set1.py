# Set

    # set represent in {}
    # Set is a mutable object, but elements of set should be immutable only
    # set does not follows index
    # set allows homogenous(same datatype) values and heterogeneous(diff datatypes) values
    # set doesnot allows duplicates
    # set function is -- set()




# set defining

x = {} # if wehen we are giving empty set it will give as empty dictionary

print(x,type(x))



x = set()

print(x,type(x))



# homogeneous

x = {10,20,30,40}
print(x,type(x))


# heterogeneous

x = {10,True,'hello',20.1}
print(x,type(x))


# duplicates

x = {10,20,30,10,20}
print(x,type(x))


# mutable

x = {10,20,30}

print(x,id(x))

y = {10,20,30}

print(y,id(y))