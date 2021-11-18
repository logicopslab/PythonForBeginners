# Initial Dictionary
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Logic',
		'App' : {1 : 'Logic', 2 : 'Ops', 3 : 'Lab'},
		'Boo' : {1 : 'YouTube', 2 : 'Course'}}
print("Initial Dictionary: ")
print(Dict)

del Dict[5]
print("\nDeleting with a specific key: ")
print(Dict)

# Deleting a Key from Nested Dictionary
del Dict['App'][3]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)
