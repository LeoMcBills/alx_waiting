class Robot:
	def __init__(self, name=None):
		self.name = name

	def say_hi(self):
		if self.name:
				print("Hi, I am a robot with a name")

		else:
				print("Hi, I am a Robot without a name")


Rob1 = Robot()
Rob2 = Robot("Haaland")

Rob1.say_hi()
Rob2.say_hi()
