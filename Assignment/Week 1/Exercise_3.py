# Exercise 3: Dictionaries

# 1: Create a dictionary

# my_dict contains three key-value pairs
my_dict = {"name":"Alex" , "age":16 , "city":"Los Angeles"}


# 2: Add a new key-value

# Adding key(gender) and value(female)
my_dict["gender"] = "Female"
print("New Key Added Dictionary: ",my_dict)     # Print New Key Added Dictionary


# 3: Update the value associated with a key

# Updating age from 16 to 18
my_dict["age"] = 18
print("Updated Dictionary: ",my_dict)          # Print Updated Dictionary


# 4: Remove a key-value pair

# Removing gender from the dictionary by using .pop() method
my_dict.pop("gender")
print("Removed key-value Dictionary: ",my_dict)        # Print Removed key-value Dictionary


# 5: Access the value associated with a specific key

# Accessing value associated with name

print("Value Associated with name is: ",my_dict["name"])    # Print Value Associated with name