"""Lambda is best used with map
---------------------------------
- let's try that out
----------------
~ r = map(func, seq)
"""

def fahrenheight(T):
    return ((float(9)/5)*T + 32)

def celsius(T):
    return (float(5)/9) * (T-32)

temperatures = (36.5, 37, 37.5, 38, 39)
F = list(map(fahrenheight, temperatures))
C = map(celsius, F)

temperatures_in_Fahrenheit = list(map(fahrenheight, temperatures))
temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenheit))
print(F)
print(temperatures_in_Fahrenheit)
print(temperatures_in_Celsius)
# print(fahrenheight(32))
# print(celsius(89.6))

print()
C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)
print()

a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]

viscius = list(map(lambda x, y, z: x + y + z, a, b, c))
print(viscius)
print()

"""Mapping a list of Functions
-------------------------------
A function that applies a bunch of functions, which maybe an iterable such as a list
or a tuple, for example, to one Python object
"""

from math import sin, cos, tan, pi
def map_functions(x, functions):
    """
    map an iterable of functions on the object x
    """
    res = []
    for func in functions:
        res.append(func(x))
    return res
family_of_functions = (sin, cos, tan)
print(map_functions(pi, family_of_functions))
print()

"""Filtering
--------------------------------
syntax- filter(function, sequence)
"""
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)
print()

even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)
print()