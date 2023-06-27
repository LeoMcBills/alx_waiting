file = open("recap.txt", "r")

for line in file:
    print(line)

file.close()

file2 = open("doesntExit.txt", "w")

file2.write("Now exists!")

file2.close()