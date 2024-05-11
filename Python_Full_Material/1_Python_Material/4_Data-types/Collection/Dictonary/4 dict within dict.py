
customer={"Name":"James","bal":50000,"Bank":"HDFC","Address":{"city":"Hyd","state":"Telangana"}}
print(customer)
print(customer['Name'])
print(customer['Address'])
print(customer['Address']['city'])


details={"Name":"Kohli","age":30,"wife":{"Name":"Anushka","age":28},"city":"Delhi"}
print(details)
print(details['wife'])
print(details['wife']['Name'])
print(details['Name'])

details["wife"]["Name"]="Alia"
print(details)






x={"cities" : ["PUNE","MUMBAI","DELHI"]}
#Task: modify or change Mumbai to Ahmedabad
print(x)
y=x["cities"]
print(y,type(y))
y[1]="Ahmedabad"
print(y)
print(x)



print("\n\n")
#changing Ahmedabad to chennai
x["cities"][1] = "chennai"
print(x)


x=10
y=x

x=20
print(x)
print(y)
                                   
                                                     
x={"students":[{"name":"James","branch":"CSE","college":"JNTU"},
               {"name":"Arjun","branch":"ECE","college":"MGIT"},
               {"name":"Alia","branch":"IT","college":"VNR"}]} 
print("\n")
print(x,len(x))
print(x["students"],type(x["students"]),len(x["students"]))

#accessing 1st dictionary----->1st student
print(x["students"][0])
#accessing particular key of a particular student
print(x["students"][2]["name"])


#accessing all students using for loop
for p in x["students"]:
    print(p)

#accessing each key of each inner dictionary ------>  James  CSE  JNTU
for p in x["students"]:
    print(p["name"],p["branch"],p["college"])
    

print("\n")
#list ,tuple within a dictionary

x={"emps":[(101,"miller",20000,"m",11),
           (102,"James",40000,"m",12),
           [103,"George",60000,"m",13],
           [104,"Kareena",90000,"f",12]]}
#printing the value(list)
print(x["emps"],type(x["emps"]),len(x['emps']))

#printing each element of the list
for p in x["emps"]:
    print(p,type(p))

#Access name and salary of George
print(x["emps"][2][1],x["emps"][2][2])

#replace the name "George" with "John"
x['emps'][2][1]="John"
print(x)

   
































