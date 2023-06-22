#!/usr/bin/python3

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(num1/num2)
except ZeroDivisionError:
    print("You made an attempt of dividing by zero. Please try again.")
else:
    print("\nEnter other numbers")
