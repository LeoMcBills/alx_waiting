#!/usr/bin/python3
import edge_cases

cards = [3, 1, 6, 5, 4, 2, 7]
choice = 5

def pick(cards, selected):
	for index, choice in enumerate(cards):
		if choice == selected:
			print(index)

print("---The Linear Search Algorithm---")
pick(cards, choice)
print("___End__")
