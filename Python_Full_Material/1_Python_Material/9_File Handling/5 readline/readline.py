#readline()

f=open("hello.txt")
print(f.tell())
print(f.readline()) #reads a particular line
f.seek(5)
print(f.tell())
print(f.readline())
f.seek(17)
print(f.tell())
print(f.readline())
f.seek(31)
print(f.tell(),f.read())
f.close() 
