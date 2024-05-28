# while loop : runs untill condition is False
# syntax:

# while <condition>:
#     .................
#     ................
#     ...while block....



# while True:
#     print('hello') # infnite loop


# print hello 5 times uing while loop

c = 0
while c<5:
    print('hello')

    c = c+1

# using for loop

for i in range(5):
    print("hello")


# extract the values from list using while loop

x = [10,20,30,40,50]

c = 0

while c<len(x):
    print(c,x[c])

    c = c+1

# extract the values from list using for loop

for i in x:
    print(i)



# extract the values from list using while loop and find value is even or odd

x = [1,2,3,4,5]

c = 0

while c<len(x):
    if x[c]%2 == 0:
        print(c,x[c])

    c = c+1