s = 'b'

substr = []

for letter in s:
    if letter in substr:
        break
    substr.append(letter)

print(substr)
print(len(substr))
