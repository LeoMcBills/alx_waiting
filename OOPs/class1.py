class Person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print(f"Hello there Mr. {self.name}")


l = Person('Leo')
l.say_hi()