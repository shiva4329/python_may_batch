
#re module defines many functions
#RegEx Functions
''' The re module offers a set of functions that allows us to search a string for a match:

Function	Description
findall	        Returns a list containing all matches
search	        Returns a Match object if there is a match anywhere in the string
sub	        Replaces one or many matches with a string 
match           for matchings  '''
#---------------------------------------------------------------------------------
#findall():
#ex:1
#1)[]---->A set of characters
#ex:[a-m]

import re

str = "python supports Dynamic datatypes"

#Find all lower case characters  between "a" and "m":

x = re.findall("[a-m]", str)  #returns list containing all matches
print(x)

print("\n")
#-------------------------------------------------------------------------------
#ex:2
#2) \d ---->any one digit

import re

#Find all digital characters from the below string

str = "Kohli scored 92 runs today out of 104 balls"



x = re.findall("\d", str)
print(x)

x = re.findall("\d{2}", str)
print(x)

x = re.findall("\d{3}", str)
print(x)
print("\n")
#--------------------------------------------------------------------------------
#ex:3
#3)^  ------>starts with
import re

str = "hello world"

#Check if the string starts with 'hello':

x = re.findall("^hello", str)
print(x,type(x),id(x))  #returns a list
if(x):
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
print("\n")
#-----------------------------------------------------------------------------------
#ex:4
#4)$ ----->ends with
import re

str = "hello world"

#Check if the string ends with 'world':

x = re.findall("world$", str)
print(x,type(x))
if (x):
  print("Yes, the string ends with 'world'")
else:
  print("No match")
print("\n")
#-------------------------------------------------------------------------------------
#ex:5
#5) * -------> 0 or more occurences of preceeding character
import re

str = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "ai" followed by 0 or more "x" characters:

x = re.findall("aix*", str)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
print("\n")
#----------------------------------------------------------------------------------------
#ex:6
#6)+ --------> 1 or more occurences
import re

str = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "ai" followed by 1 or more "x" characters:

x = re.findall("aix+", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
#----------------------------------------------------------------------------------------
#ex:7
#7) {}	Exactly the specified number of occurrences

import re

str = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "a" followed by exactly two "l" characters:

x = re.findall("al{2}", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
print("\n")                
#----------------------------------------------------------------------------------------
#ex:8
#8) |

str1="Python is easier than C Language"
#Check if the string contains either "Python" or "Java":

x = re.findall("Python|Java", str1)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
#------------------------------------------------------------------------------------------
