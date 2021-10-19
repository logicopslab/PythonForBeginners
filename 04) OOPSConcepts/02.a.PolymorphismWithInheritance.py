class Bird:
	
	def introduction(self):
		print("There are several types of birds.")

	def flight(self):
		print("Most of them can fly but a few cannot.")

class pigeon(Bird):
	
	def flight(self):
		print("Pigeons can fly.")

class ostrich(Bird):

	def flight(self):
		print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = pigeon()
obj_ost = ostrich()

obj_bird.introduction()
obj_bird.flight()

obj_spr.introduction()
obj_spr.flight()

obj_ost.introduction()
obj_ost.flight()
