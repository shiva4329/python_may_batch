

#program to accept marks of 5 subjects and compute the total and percentage
# and also compute the class/Grade awarded.

s1=90 ; s2=80 ; s3=70 ; s4=85 ; s5=75

total=s1+s2+s3+s4+s5

per=(total/500)*100

print("TOTAL=",total)
print("PERCENTAGE=",per)

if(per>=70):
    print("FIRST CLASS with Distinction")
elif(per>=60):
    print("FIRST CLASS")
elif(per>=50):
    print("SECOND CLASS")
elif(per>=40)):
    print("THIRD CLASS")
else:
    print("FAIL")
