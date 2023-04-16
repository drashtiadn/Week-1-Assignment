# Exercise 5: Loops

# 1: Fibonacci sequence

# Initialize the first two numbers in the sequence
a = 0
b = 1

# loop 10 times 
for i in range(10):
    print(a)     # Print each of them
    c = a + b
    a = b 
    b = c


# 2: Factorial of a number

# take input from the user
n = int(input("Enter any number: "))

# initialize the factorial to 1
factorial = 1

# loop from 1 to n and multiply the factorial by each number
for i in range(1,n+1):
    factorial *= i

# print the factorial of the number
print("The factorial of", n, "is",factorial)