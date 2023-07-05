"""
try:
    normal stuff

except error:
    print("MATH ERROR")
"""

number = 1

print(number * 3)

print("Do the Try and Except thing")


try:
    x = 12 / 0
    print("Wait how did you pass the exceptional checks")

except ZeroDivisionError:
    print("Dude! We don't divide numbers by zero anymore")
