

# methods

x = {'x':10,'y':20,'z':40}

# items() -- returns the each key:values pair as tuple in list
print(x.items())

# keys() -- returns only keys in list
print(x.keys())


# values() -- returns only values in list
print(x.values())

# get(key) -- returns the values of key
print(x.get('x'))


# pop(key) -- removes specific key
x.pop('y')

print(x)

#popitem() -- removes the last item in the dict

x.popitem()

print(x)

# update() # adds the item in the dictionary

x = {'x':10,'y':20}

x.update({'z':20})

print(x)
