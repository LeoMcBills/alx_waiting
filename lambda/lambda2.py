# produce a list of all alphabetical order

word = lambda listOfCharacters: ''.join(listOfCharacters)

def all_alpha():
    import string
    alpha = string.ascii_lowercase
    alpha_list = []
    for i in range(len(alpha)):
        alpha_list.append(alpha[i])

    return word(alpha_list)


""" personal summary
--------------------
1. Embed a lambda expression in both of these functions
2. Use the string module to get the alphabet
3. return the inner function
____________________
- Nice hacking!

music = lambda: print("I'm listening to music meanwhile.")

"""

def all_alpha2():
    import string
    alpha = string.ascii_uppercase
    alpha_list = []
    for i in alpha:
        alpha_list.append(i)

    return word(alpha_list)

print(all_alpha())
print(all_alpha2())

#a function to display numbers from 1 to 1000 in a table-like order
def table():
    for i in range(1, 1001):
        print(i, end=' ')
        if i % 10 == 0:
            print()

print(table())