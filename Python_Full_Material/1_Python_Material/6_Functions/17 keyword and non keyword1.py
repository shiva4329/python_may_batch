

#non-keyword arguments: In function call without parameter name giving values

#Keyword arguments : In function call,with parameter name providing values

def employee(eid,ename,sal):
    print(eid,ename,sal)

employee(101,"Miller",30000)  #non-keyword arguments
employee(eid=102,ename="JAmes",sal=50000)  #keyword arguments
employee(sal=70000,ename="Blake",eid=103)
employee(70000,103,"John") #not recommended


#default and non-default related to function definition
#keyword and non-keyword related to function call
