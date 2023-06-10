# produce a list of all alphabetical order

def all_alpha():
    import string
    alpha = string.ascii_lowercase
    alpha_list = []
    for i in range(len(alpha)):
        alpha_list.append(alpha[i])

    word = lambda: ''.join(alpha_list)
    return word()


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

    word = lambda: ''.join(alpha_list)
    return word()

print(all_alpha())
print(all_alpha2())