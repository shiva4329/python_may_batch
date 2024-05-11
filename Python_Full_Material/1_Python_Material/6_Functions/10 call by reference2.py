

#overwriting call-by-reference
def compute(list1):
    list1=[1,2,3,4,5]
    print(list1,id(list1))

list1=[10,20,30,40,50]
print(list1,id(list1))
compute(list1)
print(list1,id(list1))
