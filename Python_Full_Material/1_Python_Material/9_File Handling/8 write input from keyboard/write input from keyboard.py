#Accepting i/p from keyboard and writing into file
f=open("sample.txt",mode="w+")   #if mode="w+", it can write and read

str1=input("Enter Ur Country Name:")
f.write(str1)         #file already exists, so it truncates
f.seek(0)
print(f.read())
f.close()              #if file doesnt exist, it creates a new file

'''
f1=open("sample.txt")
print(f1.read())    
f1.close() 
'''
