#A program to multiply names and shuffle them in one given string.

import random
from random import choice as c


names = ['Kinyera', 'Nabukwasi', 'Talemwa', 'Mbaziira', 'Ninsiima']

second_names = ['Leo', 'Sheila', 'Mary', 'Victor', 'Pius', 'Doreen']


listed = []

for i in random.choices(names, k = 15):
    listed.append(i)

for j in random.choices(second_names, k = 15):
    listed.append(j)

new = random.choices(listed, k = 1000000)

newbie = " ".join(new)
print()

print(f"I {newbie} shall always remain grateful to my new upcoming skills Brethren!")

print()
