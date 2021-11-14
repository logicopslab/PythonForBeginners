
number = int(input("Enter a value: "))

sum = number + 50

# %d – integer
# %f – float
# %s – string
# %x – hexadecimal
# %o – octal
# Similar to printf() in C language

print("The sum is %d" %sum)
# print("The sum is",sum)

# Program to print a Pyramid pattern using an input()

n = int(input("Enter upto what level you want the pyramid: "))

# outer loop to handle number of rows

for i in range(0, n):  
    # inner loop to handle number of columns  
    # values is changing according to outer loop  

        for j in range(0, i + 1):  
            # printing stars  
            print("* ", end="")       
  
        # ending line after each row  
        print()