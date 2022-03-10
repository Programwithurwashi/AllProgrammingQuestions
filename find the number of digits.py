#WAP to find the the number of digits in an integer provided by user.
n=int(input("enter the number"))
count=0
while n>0:
    count+=1
    n//=10
print(count)