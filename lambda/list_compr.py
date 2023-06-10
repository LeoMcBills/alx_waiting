cards_1 = [i for i in range(11)]
cards_2 = [j for j in range(1, 11)]
print(cards_2)

print(cards_1[4:-5])

for index, card in enumerate(cards_1[4:-5]):
    print(card, end="")
    if index != 1:
        print(",", end=" ")

new_list = [2, 4, 1, 4, 2, 7]

persons = ['Pius', 'Victor', 'Natasha']

for person in persons:
    print(person)