# Creating tuples in a loop

myTuple = ('LogicOpsLab',)
n = 10 #Number of time loop runs
for i in range(int(n)):
	myTuple = (myTuple,)
	print(myTuple)
