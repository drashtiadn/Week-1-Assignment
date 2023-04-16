# Exercise 2: Lists

# 1: Create a list containing at least five elements of mixed data types

my_list = [1 , "hello" , True , ["Apple","Mango","Kiwi"] , {"name": "Alex" , "age": "16"}]

''' my_list contains five elements. 
    First element is integer (1) ,
    Second element is string ("hello") , 
    Third element is boolean (True), 
    Fourth element is list (["Apple","Mango","Kiwi"]) ,
    Fifth element is dictionary ({"name": "Alex" , "age": "16"})'''


# 2: Append a new element 

# Appending float (3.14) to the list by using .append() method
my_list.append(3.14)   
print("Appended List: ",my_list)         # Print Appended List 


# 3: Update an existing element

# Updating the list inside list (Kiwi with Banana)
my_list[3][2] = "Banana"
print("Updated List: ",my_list)         # Print Updated List 


# 4: Remove an element

# Removing string (hello) from the list using .remove() method
my_list.remove("hello")
print("Remove Element List: ",my_list)   # Print Remove Element List 


# 5: Access specific elements or a range of elements

# For specific element
print("Specific Element: ",my_list[0])     # Print the specific elements

# Using range
print("Range Element: ",my_list[1:4])  # Print element at index 1,2,3 will be output