
Di = {1: 'Logic', 'channel': 'Ops', 3: 'Lab'}

print("Accessing using key:")
print(Di['channel'])


print("Accessing using key:")
print(Di[1])

print("Accessing a element using get:")
print(Di.get(3))


# Nested Example

Dit = {'Di1': {1: 'Logic'},
		'Di2': {'Channel': 'OpsLab'}}

# Accessing element using key
print(Dit['Di1'])
print(Dit['Di1'][1])
print(Dit['Di2']['Channel'])
