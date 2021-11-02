
# initializing target string
sentence = "lab_logicopslab"

# initializing argument string
arg_string = "lab"

# using index() to find position of "logic"
# starting from various indexes

position = sentence.index(arg_string,0)
print ("The first position of lab after 0th index : ",end="")
print (position)

position = sentence.index(arg_string,5)
print ("The first position of lab after 5th index : ",end="")

print (position)


