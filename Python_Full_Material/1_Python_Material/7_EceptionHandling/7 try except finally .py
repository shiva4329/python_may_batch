#Implementing try,except and finally

try:
    x=int(input("Enter First No:"))   
    y=int(input("Enter Second No:"))  
    z=x/y
    print(z)

except(ValueError):
    print("2nd No cannot be zero") 

finally:                           # here prints msg of finally block before terminating abnormally
    print("welcome to hyd...........")
print("end")

#Try the execution for all the 3 cases ,in all 3 cases finally will be executed
