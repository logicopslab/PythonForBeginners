
catsAndBreedOrigin = {
					'Calico' : 'Egypt',
					'Aphrodite_Giant' : 'Cyprus',
					'Bambino' : 'USA',
					'Punchface' : 'Iran'
					}
					
print('List Of given cats and breeds origin:\n')

# Iterating over keys and value pairs

for cats, breed_origin in catsAndBreedOrigin.items():
    print(cats, ":", breed_origin)
    
# Nested

studentData = {
	'Student 1': {'Name': 'Ted', 'Id': 1, "Age": 34},
	'Student 2': {'Name': 'Robin', 'Id': 2, "Age": 26},
	'Student 3': {'Name': 'Medhavi', 'Id': 3, "Age": 4},
}
print("\n")

for iterator in studentData:
	
	# show
	print(studentData[iterator])