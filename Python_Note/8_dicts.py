### Dictionaries ###

# Definition

my_dict = dict()  # Define an empty dictionary
my_other_dict = {}  # Another way to define an empty dictionary

print(type(my_dict))  # Print the type of my_dict (should be dict)
print(type(my_other_dict))  # Print the type of my_other_dict

my_other_dict = {"Name": "Brais", "Last Name": "Moure", "Age": 35, 1: "Python"}

my_dict = {
    "Name": "Brais",
    "Last Name": "Moure",
    "Age": 35,
    "Languages": {"Python", "Swift", "Kotlin"},
    1: 1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))  # Print the length of my_other_dict
print(len(my_dict))  # Print the length of my_dict

# Search

print(my_dict[1])  # Access the value associated with key 1
print(my_dict["Name"])  # Access the value associated with key "Name"

print("Moure" in my_dict)  # Check if "Moure" is a key in the dictionary
print("Last Name" in my_dict)  # Check if "Last Name" is a key in the dictionary

# Insertion

my_dict["Street"] = "MoureDev Street"  # Add a new key-value pair to the dictionary
print(my_dict)

# Update

my_dict["Name"] = "Pedro"  # Update the value associated with the key "Name"
print(my_dict["Name"])

# Deletion

del my_dict["Street"]  # Delete the key "Street" and its associated value from the dictionary
print(my_dict)

# Other operations

print(my_dict.items())  # Get a view object of all key-value pairs in the dictionary
print(my_dict.keys())  # Get a view object of all keys in the dictionary
print(my_dict.values())  # Get a view object of all values in the dictionary

my_list = ["Name", 1, "Floor"]

my_new_dict = dict.fromkeys(my_list)  # Create a new dictionary with keys from my_list and default value None
print(my_new_dict)
my_new_dict = dict.fromkeys(("Name", 1, "Floor"))  # Same as above but using a tuple directly
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)  # Create a new dictionary with keys from my_dict and default value None
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, "MoureDev")  # Create a new dictionary with keys from my_dict and default value "MoureDev"
print(my_new_dict)

my_values = my_new_dict.values()  # Get a view object of all values in my_new_dict
print(type(my_values))  # Print the type of my_values

print(my_new_dict.values())  # Print the values in my_new_dict
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))  # Remove duplicates from the values and convert them to a list of keys
print(tuple(my_new_dict))  # Convert my_new_dict to a tuple of keys
print(set(my_new_dict))  # Convert my_new_dict to a set of keys
