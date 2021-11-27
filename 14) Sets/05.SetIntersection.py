# Intersection of two sets

set1 = set()
set2 = set()

for i in range(10):
	set1.add(i)
print(set1)

for i in range(8,14):
	set2.add(i)
print(set2)

# intersection() function

set3 = set1.intersection(set2)

print("\nIntersection using intersection() function")
print(set3)

# Intersection using "&" operator
set3 = set1 & set2

print("\nIntersection using '&' operator")
print(set3)
