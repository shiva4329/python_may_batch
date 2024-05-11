#Program to find the sum of first 'n' numbers

n=int(input("Enter value of n:"))

x=1
sum=0
while(x<=n):
    sum=sum+x
    x=x+1
print("Sum=",sum)
