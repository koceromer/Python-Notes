### Modules ###

import my_module

my_module.sumValue(5, 3, 1)  # Calls the sumValue function from my_module with arguments 5, 3, and 1
my_module.printValue("Hello Python!")  # Calls the printValue function from my_module with the string argument "Hello Python!"

from my_module import sumValue, printValue

sumValue(5, 3, 1)  # Calls the sumValue function directly after importing it
printValue("Hello Python")  # Calls the printValue function directly after importing it

import math

print(math.pi)  # Prints the value of pi from the math module
print(math.pow(2, 8))  # Prints the result of 2 raised to the power of 8 using the pow function from the math module

from math import pi as PI_VALUE

print(PI_VALUE)  # Prints the value of pi from the math module, using the alias PI_VALUE
