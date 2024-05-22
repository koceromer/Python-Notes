### Sets ###

# Definition

my_set = set()  # Define an empty set
my_other_set = {}  # Initially this is a dictionary

print(type(my_set))  # Print the type of my_set (should be set)
print(type(my_other_set))  # Initially this is a dictionary

my_other_set = {"Brais", "Moure", 35}  # Define a set with elements
print(type(my_other_set))  # Print the type of my_other_set

print(len(my_other_set))  # Print the length of my_other_set

# Insertion

my_other_set.add("MoureDev")  # Add an element to the set

print(my_other_set)  # Print the set (sets are unordered)

my_other_set.add("MoureDev")  # Adding a duplicate element has no effect (sets do not allow duplicates)

print(my_other_set)  # Print the set

# Search

print("Moure" in my_other_set)  # Check if "Moure" is in the set
print("Mouri" in my_other_set)  # Check if "Mouri" is in the set

# Deletion

my_other_set.remove("Moure")  # Remove an element from the set
print(my_other_set)  # Print the set

my_other_set.clear()  # Remove all elements from the set
print(len(my_other_set))  # Print the length of the set

del my_other_set  # Delete the entire set
#print(my_other_set)  # This will raise a NameError because my_other_set is no longer defined

# Transformation

my_set = {"Brais", "Moure", 35}  # Define a set
my_list = list(my_set)  # Convert the set to a list
print(my_list)  # Print the list
print(my_list[0])  # Print the first element of the list

my_other_set = {"Kotlin", "Swift", "Python"}  # Define another set

# Other operations

my_new_set = my_set.union(my_other_set)  # Union of two sets
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))  # Union with additional elements
print(my_new_set.difference(my_set))  # Difference between two sets
