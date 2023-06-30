s = 'pwwkew'
a = [*s]
substr = []
generalList = []
remover = []

num = len(a) - 1
for elem in range(num):
    for pos, letter in enumerate(a):
        if letter in substr:
            break    
        substr.append(letter)
        a.pop(pos)
    generalList.append(substr)
print(num)
print(generalList)
