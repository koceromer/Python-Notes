### Exception Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# Base exception: try except

try:
    print(numberOne + numberTwo)  # Tries to add numberOne and numberTwo
    print("No error occurred")  # If the addition is successful, this line is executed
except:
    # Executed if an exception occurs
    print("An error occurred")  # If an exception occurs during addition, this line is executed

# Full exception flow: try except else finally

try:
    print(numberOne + numberTwo)  # Tries to add numberOne and numberTwo
    print("No error occurred")  # If the addition is successful, this line is executed
except:
    print("An error occurred")  # If an exception occurs during addition, this line is executed
else:  # Optional
    # Executed if no exception occurs
    print("Execution continues correctly")  # If no exception occurs, this line is executed
finally:  # Optional
    # Always executed
    print("Execution continues")  # This line is always executed, regardless of whether an exception occurred

# Exceptions by type

try:
    print(numberOne + numberTwo)  # Tries to add numberOne and numberTwo
    print("No error occurred")  # If the addition is successful, this line is executed
except ValueError:
    print("A ValueError occurred")  # If a ValueError occurs during addition, this line is executed
except TypeError:
    print("A TypeError occurred")  # If a TypeError occurs during addition, this line is executed

# Capturing exception information

try:
    print(numberOne + numberTwo)  # Tries to add numberOne and numberTwo
    print("No error occurred")  # If the addition is successful, this line is executed
except ValueError as error:
    print(error)  # If a ValueError occurs during addition, the error message is printed
except Exception as my_random_error_name:
    print(my_random_error_name)  # If any other exception occurs during addition, the error message is printed
