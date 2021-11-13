# Example of when you expect any specific exception

def Divide_X_by_Y(x , y):
	try:
		catch = ((x+y) / (x-y))
        # 50.0 / -10.0 - Case 1
        # 60.0 / 0 -  Case 2
	except ZeroDivisionError:
		print ("x/y result in 0")
	else:
		print (catch)

# Calling Divide_X_by_Y function

# Case 1
Divide_X_by_Y(20.0, 30.0)

# Case 2
Divide_X_by_Y(30.0, 30.0)
