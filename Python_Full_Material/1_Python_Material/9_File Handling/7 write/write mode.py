#write mode
f=open("sample.txt",mode="w")
f.write("hello John...how r u??\n") #file already exists, so it truncates
f.write("Hi...")
f.close()              #if file doesnt exist, it creates a new file and writes

f1=open("sample.txt")
print(f1.read())    
f1.close()
