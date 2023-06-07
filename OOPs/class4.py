class Animals:

    population = 0

    def __init__(self, name, habitable=False):
        self._name = name
        self.__habitable = habitable

    def getter(self):
        return self.__habitable

rep = Animals("Dog", True)

print(rep._name)

# Access the private attribute

print(rep.getter())