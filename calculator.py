from more_itertools import divide
from numpy import multiply, subtract


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def div(a, b):
    return a/b


def mul(a, b):
    return a*b


print("first calculator")
print("Choose the operation to perform")
print("1.  Addition")
print("2.  Subtract")
print("3.  Division")
print("4.  Multiplication")
while True:
    choice = input("Enter your choice")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("enter the first number"))
        num2 = float(input("enter the second  number"))
        if choice == '1':
            print("The result is", add(num1, num2))
        elif choice == '2':
            print("The result is", subtract(num1, num2))
        elif choice == '3':
            print("The result is", divide(num1, num2))
        elif choice == '4':
            print("The result is", multiply1(num1, num2))
    else:
        print("wrong choice")
