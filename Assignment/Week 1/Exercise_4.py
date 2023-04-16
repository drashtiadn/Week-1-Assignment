# Exercise 4: Conditional Statements

# 1: Checks if a number is positive, negative, or zero

# Using  if , elif , else statement with try , except and else

# User will enter the number
num = input("Enter any number: ")  

# Convert input into float
try:
    num = float(num)
except ValueError:
     #  If the input is not a valid integer, the program will print an error message. 
    print("Invalid Input. Please enter a number!")
else:
    #  Checks if a number is positive, negative, or zero
    if num == 0:
        print("The number is Zero!")

    elif num > 0:
        print("The number is Positive!")

    else:
        print("The number is Negative!")