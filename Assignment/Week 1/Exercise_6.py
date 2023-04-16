# Exercise 6: Functions

# 1: Two numbers as arguments and returns their sum

def add_numbers(a, b):
    return a + b

# 2:  Average of a list of numbers
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# 3: Call the functions with sample inputs
result1 = add_numbers(7,9)
result2 = calculate_average([2, 4, 6, 8, 10])

# Display the results
print("Result of adding two numbers: ", result1)
print("Result of calculating average: ", result2)