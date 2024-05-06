# string slicing : breaking the string



# index = forward index --- left to right -- 0
        # backward index --- right to left -- -1




# string


x = 'python'

print(len(x))


# extract the 'o' ins tring using +ve index

print(x[4])

print(x[3])

print(x[0])

# -ve index

print(x[-2])

print(x[-1])



# string slicing

x = 'python'

# etract 'yth'

# syntax: [start:end-1]

print(x[1:3])

print(x[1:4])


# using -ve index
print(x[-3:-5]) # returns empty

# note : lower(start) bound should be lesser than upper(end) bound
print(x[-5:-2])



# etract 'thon' negative index

print(x[-4:-1])

print(x[-4:0]) # returns empty

print(x[-4:]) # note : upper bound is empty -- prints till end of the string

# what if lower bound is empty

# prints starting of the string

print(x[:4])

# what if both lower and upper is empty

print(x[:]) # prints entire string






# 'welcome to python'

# extract 'python' using +ve index
# extarct 'welcome' using -ve index
# extract 'come to' using both -ve and +ve index

# convert whole string into upper case

# split the string