#fibonacci series 
n=int(input("Enter the nm  "))
lst=[0]*n
lst[0]=0
lst[1]=1
for i in range(2,n):
    lst[i]=lst[i-1]+lst[i-2]
for i in range(n):
    print(lst[i],end=' ')