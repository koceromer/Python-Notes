### Conditionals ###

# if

my_condition = False

 # It's the same as if my_condition == True:
if my_condition:  # If the condition is True, execute the following block of code
    print("The if condition is executed")

my_condition = 5 * 5  # Calculate the value of my_condition

if my_condition == 10:  # If my_condition is equal to 10, execute the following block of code
    print("The condition of the second if statement is executed")

# if, elif, else

if my_condition > 10 and my_condition < 20:  # If my_condition is greater than 10 and less than 20, execute the following block of code
    print("It is greater than 10 and less than 20")
elif my_condition == 25:  # If my_condition is equal to 25, execute the following block of code
    print("It is equal to 25")
else:  # If none of the above conditions are met, execute the following block of code
    print("It is less than or equal to 10, or greater than or equal to 20, or not equal to 25")

print("Execution continues")  # This line will be executed regardless of the conditions above

# Conditional with value inspection

my_string = ""

if not my_string:  # If my_string is empty (or evaluates to False), execute the following block of code
    print("My string is empty")

if my_string == "My stringggggg":  # If my_string is equal to "My stringggggg", execute the following block of code
    print("These strings match")
