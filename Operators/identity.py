# 6 .identity operators

#     is

#     is not

# note : identity operators are based on value address

# is

x = 10
print(id(x))

y = 10
print(id(y))

print(x is y) # it checks the memory address
print(x == y) # it checks the value


x = [10,20]
print(id(x))

y = [10,20]
print(id(y))

print(x is y)

print(x == y)



# is not


x = [10,20]
print(id(x))

y = [10,20]
print(id(y))

print(x is not y) # checks on address

print(x != y) # checks on data

