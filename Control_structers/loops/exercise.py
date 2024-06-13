# x = ['a','b','c','d'] find the vowels using both for and while loop
# x = range(1,50) find the number which is divisible by 5 using both for and while loop
# x = 101 check if palindrome or not
# x = 'madam' check if palindrome or not



# using while loop
x = ['a','b','c','d','e','l','u']

c = 0

while c<len(x): # while loop rotates until c < 7 after that while loop stops the rotation
    # print(x[c])
    if x[c] in 'aeiou':
        print(x[c], 'is vowel')
    c +=1

# x = range(1,50) find the number which is divisible by 5 using both for and while loop

x = list(range(1,50))
print((x))

c = 0

while c < len(x):
    if x[c]%5 == 0:
        print(x[c],end=',')

    c += 1


