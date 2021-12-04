# read() mode
myfile = open("logicopslab.txt", "r")
print (myfile.read())

# Character wise
myfile_1 = open("logicopslab.txt", "r")
print (myfile_1.read(10))

# Read and Write

myfile_2 = open(r"C:/Users/ravis/Desktop/PythonForBeginners/15) FileHandling/logicopslab.txt", "r+")

#The open method opens the file and returns a TextIOWrapper object but does not read the files content.

print(myfile_2.read())
myfile_2.close()