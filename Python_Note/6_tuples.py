### Tuples ###

# Definition

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

# Accessing elements and searching

print(my_tuple[0])  # Access the first element
print(my_tuple[-1])  # Access the last element
#print(my_tuple[4])  # IndexError: Index out of range
#print(my_tuple[-6])  # IndexError: Index out of range

print(my_tuple.count("Brais"))  # Count the occurrences of "Brais" in the tuple
print(my_tuple.index("Moure"))  # Get the index of "Moure"
print(my_tuple.index("Brais"))  # Get the index of the first occurrence of "Brais"

#my_tuple[1] = 1.80  # 'tuple' object does not support item assignment

# Concatenation

my_sum_tuple = my_tuple + my_other_tuple  # Concatenate two tuples
print(my_sum_tuple)

# Subtuples

print(my_sum_tuple[3:6])  # Get a subtuple from index 3 to 5

# Mutable tuple with conversion to list

my_tuple = list(my_tuple)  # Convert the tuple to a list
print(type(my_tuple))

my_tuple[4] = "MoureDev"  # Modify the list
my_tuple.insert(1, "Blue")
my_tuple = tuple(my_tuple)  # Convert the list back to a tuple
print(my_tuple)
print(type(my_tuple))

# Deletion

#del my_tuple[2]  # TypeError: 'tuple' object doesn't support item deletion

del my_tuple  # Delete the entire tuple
#print(my_tuple)  # NameError: name 'my_tuple' is not defined
