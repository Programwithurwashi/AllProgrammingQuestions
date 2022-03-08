#WAP to tell whether a number is positive or negative or neutral.
n=float(input("Enter the number"))
if n>0:
     print("Entered number is positive number")
elif n<0:
    print("Entered number is negative")
elif n==0:
    print("Entered number is neutral")
else:
    print("Wrong input")