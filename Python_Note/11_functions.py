### Functions ###

# Definition

def my_function():
    print("This is a function")

my_function()
my_function()
my_function()

# Function with input parameters/arguments

def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)  # Prints the sum of 5 and 7
sum_two_values(54754, 71231)  # Prints the sum of 54754 and 71231
sum_two_values("5", "7")  # Tries to concatenate strings "5" and "7"
sum_two_values(1.4, 5.2)  # Prints the sum of 1.4 and 5.2 as a float

# Function with input parameters/arguments and return value

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(1.4, 5.2)  # The result is not saved
print(my_result)  # This will print None because the function does not return a value

my_result = sum_two_values_with_return(10, 5)  # The result is saved
print(my_result)  # This will print the result of the function call

# Function with keyword arguments

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Moure", name="Brais")

# Function with default arguments

def print_name_with_default(name, surname, alias="No alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure")  # Prints "Brais Moure No alias"
print_name_with_default("Brais", "Moure", "MoureDev")  # Prints "Brais Moure MoureDev"

# Function with arbitrary arguments

def print_upper_texts(*texts):
    print(type(texts))  # Prints the type of texts, which is tuple
    for text in texts:
        print(text.upper())  # Prints each text in uppercase

print_upper_texts("Hello", "Python", "MoureDev")  # Prints each text in uppercase
print_upper_texts("Hello")  # Prints "HELLO"
