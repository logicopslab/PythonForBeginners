# Creating an empty Dictionary
MyDictionary = {}
print("Empty Dictionary: ")
print(MyDictionary)

MyDictionary[0] = 'Logic'
MyDictionary[2] = 'Ops'
MyDictionary[3] = 10
print("\nDictionary after adding 3 elements: ")
print(MyDictionary)

# Updating

MyDictionary[2] = 'Welcome'
print("\nUpdated key value: ")
print(MyDictionary)

# Adding Nested Key value

MyDictionary[5] = {'Nested' :{'10' : 'Bravo', '20' : 'Lab'}}
print("\nAdding a Nested Key: ")
print(MyDictionary)
