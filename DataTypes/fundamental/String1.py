# string - combination of letters
    # python fn - str()
    # represents in - single/double quotes -- '...'/ "....."


# in python string can be single letter or combination of letters


# single char
x = 'a'

print(x)
print(type(x))


# multi char
x = 'hello'

print(x)
print(type(x))


# string functions

x = 'python'

print(x)
print(type(x)) # returns the type of data

# length oof string 
print(len(x))

# id() - returns the memory address of data
print(id(x))


# string methods

x = 'python'

# upper()
print(x.upper())

# lower()
print(x.lower())

x = 'pYtHoN'

#swapcase()

print(x.swapcase())

# strip() -- removes extra spaces before and after the string

x = '    hello python      '

print(x.strip())

# lstrip() -- removes extra spaces begining of the string

x = '    hello python      '
print(x.lstrip())

# rstrip() -- removes extra spaces ending of the string

x = '    hello python      '
print(x.rstrip())


# split()

x = 'hello python'

print(x.split())

x = 'hello,python'

print(x.split(','))

x = 'hello@python@hai'

print(x.split('@'))
