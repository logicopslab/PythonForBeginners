
MyDictionary_01 = {1: 'Logic', 2: 'Ops', 3: 'Lab'}
print("\nDictionary using Integer as Keys: ")
print(MyDictionary_01)


MyDictionary_02 = {'ChannelName': 'LogicOpsLab', 1: [1, 2, 3, 4, 5, 6]}
print("\nDictionary using Mixed Keys: ")
print(MyDictionary_02)


# Creating through dict() function

MyDictionary_03 = dict({1: 'Logic', 2: 'Ops', 3:'Lab'})
print("\nDictionary using dict() function: ")
print(MyDictionary_03)

# Duplicate Keys

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "years": 2020
}
print("Make sure the Keys are not the same\n",thisdict)