#WAP to print if a number is divisible by 2 0r 3 0r both
num=int(input("Enter the number"))
if num%6==0:
    print(num,"Number is divisible by 2 and 3 both")
elif num%2==0:
    print(num,"number is divisible by 2 also")
elif num%3==0:
    print(num,"number is divisible by 3 also")
else:
    print(num,"number is neither divisible by 2 nor 3")