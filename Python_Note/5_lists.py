### Lists ###

# Definition

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]

print(type(my_list))
print(type(my_other_list))

# Accessing elements and searching

print(my_other_list[0])  # Access the first element
print(my_other_list[1])  # Access the second element
print(my_other_list[-1])  # Access the last element
print(my_other_list[-4])  # Access the fourth from last element
print(my_list.count(30))  # Count the occurrences of 30 in the list
#print(my_other_list[4])  # IndexError: Index out of range
#print(my_other_list[-5])  # IndexError: Index out of range

print(my_other_list.index("Brais"))  # Get the index of "Brais"

age, height, name, surname = my_other_list  # Unpack the list into variables
print(name)  # Print the name

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]  # Unpack specific elements into variables
print(age)  # Print the age

# Concatenation

print(my_list + my_other_list)  # Concatenate two lists
#print(my_list - my_other_list)  # TypeError: unsupported operand type(s) for -: 'list' and 'list'

# Creation, insertion, updating, and deletion

my_other_list.append("MoureDev")  # Append an element to the list
print(my_other_list)

my_other_list.insert(1, "Red")  # Insert an element at a specific index
print(my_other_list)

my_other_list[1] = "Blue"  # Update an element at a specific index
print(my_other_list)

my_other_list.remove("Blue")  # Remove the specified element
print(my_other_list)

my_list.remove(30)  # Remove the first occurrence of 30
print(my_list)

print(my_list.pop())  # Remove and return the last element
print(my_list)

my_pop_element = my_list.pop(2)  # Remove and return the element at index 2
print(my_pop_element)
print(my_list)

del my_list[2]  # Delete the element at index 2
print(my_list)

# List operations

my_new_list = my_list.copy()  # Create a shallow copy of the list

my_list.clear()  # Remove all elements from the list
print(my_list)
print(my_new_list)

my_new_list.reverse()  # Reverse the order of the list
print(my_new_list)

my_new_list.sort()  # Sort the list
print(my_new_list)

# Sublists

print(my_new_list[1:3])  # Get a sublist from index 1 to 2

# Type conversion

my_list = "Hello Python"
print(my_list)
print(type(my_list))
