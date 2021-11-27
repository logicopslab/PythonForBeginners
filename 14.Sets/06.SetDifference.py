set1 = set()
set2 = set()

for i in range(10):
	set1.add(i)
print(set1)

for i in range(8,14):
	set2.add(i)
print(set2)

# difference() function

set3 = set1.difference(set2)

print("\nDifference using difference() function :",set3)

# '-' operator
set3 = set1 - set2

print("\nDifference using '-' operator :", set3)

# Symmetric Difference

set4 = set1.symmetric_difference(set2)
print("\nSymmetric Difference :", set4)
