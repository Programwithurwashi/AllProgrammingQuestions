#WAP to tell whether an year is leap year or not.
n=int(input("WEnter the year"))
if n%4==0:
    print("Year is a leap year")
elif n%400==0:
    print("Year is a leap year")
elif n%100!=0:
    print("Year is not leap year")
else:
    print("no is not leap year")