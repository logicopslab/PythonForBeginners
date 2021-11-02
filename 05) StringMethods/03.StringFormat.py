
# Multiple placeholders in format() function
your_string = "{} is a {} youtube channel for {}"
print(your_string.format("LogicOps Lab", "DevOps", "and SRE"))

# different datatypes in formatting
print("Hello! My name is {} and I have {} years of exp"
	.format("Ravish", 9.6))

print("-----------------------------------------")

# Formatters with Positional and Keyword Arguments


print("{0} Ops {1}!!".format("Logic","Lab"))

# Changing index numbers with params of the placeholders
print("{1} Ops {0}!!".format("Logic","Lab"))

# When placeholders { } are empty, Python will replace the 
# values passed through str.format() in order.

print("Every {} must know {} or {} and {}"
	.format("DevOps/SRE", "Coding", "Scripting",
			"System Design"))


# Use the index numbers of the values to change the order 
# that they appear in the string
print("Every {3} MUST know {2} {1} or {0}"
	.format("DevOps/SRE", "Coding", "Scripting", "System Design"))


# Keyword arguments are called
# by their keyword name
print("{lol} is the {0} YouTube channel for {1}"
	.format("BEST", "DevOps/SRE", lol="LogicOpsLab"))

