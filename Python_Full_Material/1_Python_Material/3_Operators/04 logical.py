#Logical Operators: These operators gives logical relationship b/w 2 objects
'''
These operators also returns either True/False.

The various logical operators are:
    i)and
    ii)or
    iii)not

        x        y        x and y        x or y
        True     True     True           True
        True     False    False          True
        False    True     False          True
        False    False    False          False  '''


x=10
y=20
z=30

p=(x>y) and (y<=z)
print(p)

q=(x>z) and (y!=z) or (z>x)   
print(q)

r=(x>=z) and (z==x+y) or (y==z-x) or (y>=z)
print(r)

print(not True)
print(not False)













