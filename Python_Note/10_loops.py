### Loops ###

# While

my_condition = 0

while my_condition < 10:  # Execute the block as long as the condition is true
    print(my_condition)  # Print the current value of my_condition
    my_condition += 2  # Increment my_condition by 2 in each iteration
else:  # Optional else block executed when the while condition becomes false
    print("My condition is greater than or equal to 10")

print("Execution continues")

while my_condition < 20:  # Another while loop example
    my_condition += 1  # Increment my_condition by 1 in each iteration
    if my_condition == 15:  # If my_condition reaches 15
        print("Execution stops")  # Print a message
        break  # Exit the loop
    print(my_condition)  # Print the current value of my_condition

print("Execution continues")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:  # Iterate over each element in the list
    print(element)  # Print the current element

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")

for element in my_tuple:  # Iterate over each element in the tuple
    print(element)  # Print the current element

my_set = {"Brais", "Moure", 35}

for element in my_set:  # Iterate over each element in the set
    print(element)  # Print the current element

my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

for element in my_dict:  # Iterate over each key in the dictionary
    print(element)  # Print the current key
    if element == "Edad":  # If the key is "Edad"
        break  # Exit the loop
else:  # Optional else block executed when the for loop completes without encountering a break
    print("The for loop for the dictionary has ended")

print("Execution continues")

for element in my_dict:  # Another for loop example with dictionary
    print(element)  # Print the current key
    if element == "Edad":  # If the key is "Edad"
        continue  # Skip the remaining code and continue with the next iteration
    print("This is executed")
else:  # Optional else block executed when the for loop completes without encountering a break
    print("The for loop for the dictionary has ended")
