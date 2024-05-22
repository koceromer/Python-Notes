# Variables

# Define a string variable and print it
my_string_variable = "My String variable"
print(my_string_variable)

# Define an integer variable and print it
my_int_variable = 5
print(my_int_variable)

# Convert the integer variable to a string and print it along with its type
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Define a boolean variable and print it
my_bool_variable = False
print(my_bool_variable)


# Concatenating variables in an output
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("This value:", my_bool_variable)


# Some system functions
# Use len() to get the length of a string variable
print(len(my_string_variable))


# Variables in a single line. Be careful not to abuse this syntax!
# Define multiple variables in a single line
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
print("My name is:", name, surname, ". My age is:", age, ". My alias is:", alias)


# Inputs
# Get user input for name and age
name = input('What is your name? ')
age = input('How old are you? ')
print(name)
print(age)

# Changing their type
# Change the type of variables
# Change the type of name and age variables
name = 35
age = "Brais"
print(name)
print(age)

# Forcing the type?
# Force a variable to a specific type
# Change the type of address variable multiple times
address: str = "My address"
address = True
address = 5
address = 1.2
print(type(address))
