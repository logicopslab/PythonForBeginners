class Doge:

	# class attribute
	attr1 = "Good Boi!!"

	# Instance attribute
	def __init__(self, name):
		self.name = name

# Driver code
# Object instantiation
Chibba = Doge("Chibba")
Hachiko = Doge("Hachiko")

# Accessing class attributes
print("Chibba is a {}".format(Chibba.__class__.attr1))
print("And, Hachiko is also a {}".format(Hachiko.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Chibba.name))
print("My name is {}".format(Hachiko.name))
