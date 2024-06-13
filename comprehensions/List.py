# list comprehension
# creates the list in single line

# create  a list with 10 numbers

x = []

for i in range(1,11):
    x.append(i)

print(x)


x = [i for i in range(1,11)]

print(x)

# create a list with even numbers

x = [i for i in range(1,11) if i%2 == 0]

print(x)


