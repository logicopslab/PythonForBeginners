# Creating a Dictionary
Dict = {1: 'Logic', 'channel': 'LL', 3: 'Lab'}

print('\nDictionary before deletion: ',Dict)

# Deleting using pop() method
pop_returns = Dict.pop(1)
print('\nDictionary after deletion: ' + str(Dict))
print('Returned popped key is:',pop_returns)
