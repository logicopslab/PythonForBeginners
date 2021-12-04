# Opening a file

myfile1 = open('logicopslab3.txt', 'w')
Lt = ["Logic \n", "Ops \n", "Lab \n"]
st = "Hello\n" #\n is new line

# Writing a string
myfile1.write(st)

# Writing multiple strings

myfile1.writelines(Lt)

myfile1.close()

# Checking the data

myfile1 = open('logicopslab3.txt', 'r')
print(myfile1.read())
myfile1.close()
