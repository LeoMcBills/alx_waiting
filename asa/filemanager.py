file = open("Greatest.txt", "r")

for line in file:
    print(line, end='')

file.close()

file = open("Greatest.txt", "a")

file.write("\nThis actually works!")

file = open("Greatest.txt", "r")

for line in file:
    print(line, end="")

file.close()