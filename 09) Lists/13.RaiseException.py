# Manually Raising an Exception

try:
	# Raise Error
    raise NameError("Hello, World") 
    
except NameError:
	print ("This is a manually raised exception")