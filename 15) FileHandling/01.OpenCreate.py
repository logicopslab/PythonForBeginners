# Opening a file

myfile = open("logicopslab.txt")

# Reading from file
print(myfile.read())

# creating a new empty file
newFile = open("a_new_file.txt", "x")

myfile.close()
newFile.close()