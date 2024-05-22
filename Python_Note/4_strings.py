### Strings ###

# Define string variables
my_string = "My String"  # Define a string variable
my_other_string = 'My other String'  # Define another string variable

# Get the length of the strings
print(len(my_string))  # Print the length of the first string
print(len(my_other_string))  # Print the length of the second string

# Concatenate strings
print(my_string + " " + my_other_string)  # Concatenate the two strings and print

# String with newline character
my_new_line_string = "This is a String\nwith a newline"  # Define a string with a newline character
print(my_new_line_string)  # Print this string

# String with tab character
my_tab_string = "\tThis is a String with a tab"  # Define a string with a tab character
print(my_tab_string)  # Print this string

# Escaped string
my_scape_string = "\\tThis is an \\n escaped String"  # Define a string with escaped characters
print(my_scape_string)  # Print this string

# Formatting

name, surname, age = "Brais", "Moure", 35  # Define variables for name, surname, and age
print("My name is {} {} and I am {}".format(name, surname, age))  # Print a formatted output using format()
print("My name is %s %s and I am %d" %(name, surname, age))  # Print a formatted output using % operator
print("My name is " + name + " " + surname + " and I am " + str(age))  # Print a formatted output using string concatenation
print(f"My name is {name} {surname} and I am {age}")  # Print a formatted output using f-string

# Unpacking characters

language = "python"  # Define the string "python"
a, b, c, d, e, f = language  # Unpack the characters of "python" into variables
print(a)  # Print the first character
print(e)  # Print the fifth character

# Slicing

language_slice = language[1:3]  # Get a slice of "python"
print(language_slice)  # Print the slice

language_slice = language[1:]  # Get the slice from the first character to the end
print(language_slice)  # Print the slice

language_slice = language[-2]  # Get the second last character
print(language_slice)  # Print the character

language_slice = language[0:6:2]  # Get a slice from 0 to 6 with a step of 2
print(language_slice)  # Print the slice

# Reverse

reversed_language = language[::-1]  # Reverse the string "python"
print(reversed_language)  # Print the reversed string

# String methods

print(language.capitalize())  # Capitalize the string
print(language.upper())  # Convert the string to uppercase
print(language.count("t"))  # Count occurrences of "t" in the string
print(language.isnumeric())  # Check if the string is numeric
print("1".isnumeric())  # Check if this character is numeric
print(language.lower())  # Convert the string to lowercase
print(language.lower().isupper())  # Check if all characters are lowercase
print(language.startswith("Py"))  # Check if the string starts with "Py"
print("Py" == "py")  # Check if "Py" is equal to "py"
