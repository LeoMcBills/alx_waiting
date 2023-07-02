pumpkins = [1, 2, 3, 4, 5]

def squarer(pumpkins):
    new = []
    for index, i in enumerate(pumpkins):
        n = i ** 2
        new.append(n)
    return new

tester = map(squarer, squarer)
print(tester)


