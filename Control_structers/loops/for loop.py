# for loop : iterates until sequences completed

x = 'python'
for i in x:
    print(i)



x = [10,20,30,40]

for i in x:
    print(i)


x = (10,20,30)
for i in x:
    print(i)


# create a list with 100 values

# print(range(100))

# print(range(1,100))

# for i in range(1,100):
#     print(i)

x = []

for item in range(1,100):
    x.append(item)# adds the values into list

print(x)


# find the even numbers in thelist

x = [1,2,3,4,5]

for i in x:
    if i%2 == 0:
        print(i,'even number')
    else:
        print(i)

# find the vowels in the list

x = ['a','b','c','d','e']

for i in x:
    if i in 'aeiou':
        print(i,'vowel')
    else:
        print(i)



# create a list only having even numbers

x = range(100)

y = []

for i in x:
    if i%2 == 0:
        y.append(i)

print(y)



# create a list only having odd numbers

x = range(100)

y = []

for i in x:
    if i%2 != 0:
        y.append(i)

print(y)


# 