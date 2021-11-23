# Python3 code to iterate through all keys in a dictionary

catsAndBreedOrigin = {
					'Calico' : 'Egypt',
					'Aphrodite_Giant' : 'Cyprus',
					'Bambino' : 'USA',
					'Punchface' : 'Iran'
					}
					
print('List Of given Cats:\n')

# Iterating over keys
for cats in catsAndBreedOrigin:
	print(cats)

# Nested

studentData = {
	'Student 1': {'Name': 'Ted', 'Id': 1, "Age": 34},
	'Student 2': {'Name': 'Robin', 'Id': 2, "Age": 26},
	'Student 3': {'Name': 'Medhavi', 'Id': 3, "Age": 4},
}
print("\n")
for iterator in studentData:
	# show
	print(studentData[iterator].keys())
