class SchoolMember:
    """Represents any school member."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Initialized School Member: {self.name}")

    def tell(self):
        """Tell my details."""
        print(f"Name: '{self.name}' and Age: '{self.age}'")
        

class Teacher(SchoolMember):
    """Represents a teacher..."""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print(f"Initialized Teacher: {self.name}")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Salary: '{self.salary}'")


class Student(SchoolMember):
    "Represents a student..."
    