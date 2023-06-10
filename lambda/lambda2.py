# produce a list of all alphabetical order

def all_alpha():
    import string
    alpha = string.ascii_lowercase
    alpha_list = []
    for i in range(len(alpha)):
        alpha_list.append(alpha[i])

    word = ','.join(alpha_list)
    return word

def all_alpha2():
    import string
    alpha = string.ascii_uppercase
    alpha_list = []
    for i in alpha:
        alpha_list.append(i)

    word = ','.join(alpha_list)
    return word

print(all_alpha())
print(all_alpha2())