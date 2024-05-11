#Q) how to merge 2 lists
#Q) how to convert a list to dictionary

#using zip() function, we can merge 2 lists and
# after merging convert it to dictionary

subjects=["Eng","maths","phy","chem"]
marks=[90,95,75,85]

#now using zip() merge the 2 lists
x=zip(subjects,marks)
print(x,type(x))

#convert this zip to list

y=list(x)
print(y,type(y))

#now convert this list to dictionary
z=dict(y)
print(z,type(z))


#Note: Zip is a iterator object , where we can iterate only once
#Once we perform an operation on a zip object , it gets exhausted i.e it will be empty
'''
