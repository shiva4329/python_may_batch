#Accepting keys and values of a dictionary from  the user keyboard

subject=[]
marks=[]

print("Enter names of 5 Subjects as keys")

for p in range(0,5):
    key=input("Enter name of subject"+str(p+1)+":")
    subject.append(key)
    
print("Enter marks of 5 subjects as values")

for p in range(0,5):
    value=int(input("Enter marks of"+subject[p]+":"))
    marks.append(value)

print(subject)
print(marks)

print("Total marks=",sum(marks))

x=zip(subject,marks)
print(x,type(x))

y=dict(x)
print(y,type(y))
