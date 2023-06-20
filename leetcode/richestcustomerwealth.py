rich = {"Elon Musk":"280M", "Jeff Benzos":"176M", "Bernault Ashault":"297M"}

i = 0

for person in rich.items():
   # print(person)
    listThem = []
    listThem[i] += person
    i += 1
    if i == 2:
        break

print(listThem)
