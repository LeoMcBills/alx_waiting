import timeit

"""Practice for all that has been learnt so far
----------
- lambda
- map
- filter
-------
use them in any program
"""

buddies = ['Victor', 'Essay', 'Byenkya', 'Allan', 'Asiimwe', 'Ian', 'Muyenzi', 'Pius', 'Mbaziira']

# a function that says hi to everyone who's name has been acquired
def say_hi(names):
    print()
    for name in names:
        print(f"Hi there {name}, it's been quite a long time")
    print()

say_hi(buddies)

x = [i for i in range(11)]

y = lambda x: [i for i in x], print(x)
print(x)

print()
y
print()

multiply = lambda x, y: print(x * y)

multiply(2, 3)
print()