#String Operations:
#String methods:
#1.s.upper() : For converting a string to upper case
x="good morning"
print(x.upper())
print(x)

#2.s.lower() : For converting a string to lower case
y="PYTHON"
print(y.lower())

#3.replace():for replacing a portion of a string
x="java is easy"
print(x)
y=x.replace("java","python")
print(y)
print(x)

#4.split() : For splitting a line into list of words
line="python is simple"
print(line,type(line))
words=line.split(" ")
print(words,type(words))

#Task: I want to print mumbai
cities="hyd,pune,chennai,mumbai"
print(cities,type(cities))

res=cities.split(",")
print(res,type(res))
print(res[3])

#5.strip():removes blank spaces at the beginning and at the end of the string
x="    python is easy       "
print(x)
y=x.strip()
print(y)

#6.startswith(string)
#   endswith(string)

line="python is easy"
print(line.startswith("python"))
print(line.endswith("easy"))

#7.find(string): returns starting index position if found ,else returns -1
z="python is simple"
print(z.find("simple"))

#8.count() : returns the count of a character or sub-string

x="hello hello hello ..... how r u?"
print(x.count("hello"))
print(x.count("h"))

#9.capitalize() :capitalizes the first character of a string
x="india"
print(x.capitalize())

#string functions:
#1.len():Returns the length of a string
x="India"
print(x)
print(len(x))

#2.max(): returns the max character of a string
x="hello"
print(max(x))

#3.min():returns the min character of a string
print(min(x))

#String special characters:
#1.+ :String concatenation
x="hello world"
print((x[0:5]).capitalize()+" "+"India")

#2.* :Repeatition
x="hello"
print(x*3)

#3.[ ] :String index
x="python"
print(x[2])

#4.[ : ]:slicing
print(x[0:3])

#5.in or not in
x="python"
print('P' in x)
print('f' in x)
print('f' not in x)

































































