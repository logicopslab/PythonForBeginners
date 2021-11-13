
try:
	k = 2//0 # this will raise divide by zero exception.
	print(k)

# handles exception
except ZeroDivisionError:
	print("You just can't divide by 0")

finally:
	# Always gets executed regardless of exception raised.
	print('Make sure you write your programs carefully!')
