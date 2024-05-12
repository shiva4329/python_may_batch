# defining dictinary
# syntax = {key:value}




x = {} # empty dictionary

print(x,type(x))


#

x = {'name':'siva','marks':100,'age':50}

print(x)
print(len(x))
print(id(x))
print(type(x))


# duplicates
# dictionay dosent allows duplicate keys and it allows duplicate values

x = {'x':10,'y':20,'x':100,'z':10} # when we are using duplicate keys it will take latest value

print(x)

#keys and values can be either homogeneous or heterogeneous.


x = {1:'hello','x':100,10.1:500} # True is nothing but 1

print(x)


