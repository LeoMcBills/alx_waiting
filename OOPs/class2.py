class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        self.name = name
        print(f"Initializing: {self.name}")

        #adds to the population
        Robot.population += 1


    def die(self):
        """I am dying."""
        
        print(f"{self.name} is being killed")

        Robot.population -= 1

        if Robot.population == 0:
            print(f"{self.name} was the last one")
        else:
            print(f"There are still {Robot.population} robots still working")

    
    def say_hi(self):
        """Greeting by the Robot
        
        Yeah! they can do that."""
        print(f"Greetings! my masters call me {self.name}")


    @classmethod
    def how_many(cls):
        """Prints the current population."""
        if cls.population == 1:
            print(f"We have 1 Robot.")
        print(f"We have {cls.population} Robots.")
    

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

print()
droid2 = Robot("R2-D3")
droid2.say_hi()
Robot.how_many()

print()
droid3 = Robot("F1-D1")
droid3.say_hi()
Robot.how_many()