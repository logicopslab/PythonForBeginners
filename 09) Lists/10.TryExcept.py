animals = ['dog', 'deer', 'cat', 'snake']
try:
    cat_index = animals.index('cats')
except:
    cat_index = 'No cats found!!'
print(cat_index)