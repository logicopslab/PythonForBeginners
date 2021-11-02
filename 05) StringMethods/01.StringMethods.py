
your_text = 'lOgiC oPs LAB'

# upper() function to convert string to upper_case

print("Uppercase String:")
print(your_text.upper())

# lower() function to convert string to upper_case
print("Lowercase String:")
print(your_text.lower())

# space breaks the string
print("Title String:")
print(your_text.title())

# original string never changes
print("Raw String")
print(your_text)

# returns False
returned_value = your_text.endswith('LABS')
print (returned_value)
  
# returns True
returned_value = your_text.endswith('LAB')
print (returned_value)

# returns False
returned_value = your_text.startswith('LoGic')
print (returned_value)
  
# returns True
returned_value = your_text.startswith('lOgiC')
print (returned_value)
