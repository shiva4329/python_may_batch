# break = breaks the loop
# continue = skips the current iteration
# pass = does nothing

# break

# break loop when number is 5

x = list(range(1,10))
print(x)
for i in x:
    # print(i)
    if i == 5:
        break
    print(i)
    print('hello')

# continue
# skips the iteration when number is 5
x = list(range(1,10))
print(x)
for i in x:
    # print(i)
    if i == 5:
        continue
    print(i)
    print('hello')

# pass

x = list(range(1,10))
print(x)
for i in x:
    # print(i)
    if i == 5:
        pass
    print(i)
    # print('hello')


#
if True:
    pass