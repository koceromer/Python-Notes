### Arithmetic Operators ###

# Operations with integers
print(3 + 4)  # Addition
print(3 - 4)  # Subtraction
print(3 * 4)  # Multiplication
print(3 / 4)  # Division
print(10 % 3)  # Modulus (remainder of division)
print(10 // 3)  # Floor division (quotient without remainder)
print(2 ** 3)  # Exponentiation
print(2 ** 3 + 3 - 7 / 1 // 4)  # Complex expression

# Operations with strings
print("Hello " + "Python " + "How are you?")  # Concatenation
print("Hello " + str(5))  # Concatenation with conversion

# Mixed operations
print("Hello " * 5)  # String repetition
print("Hello " * (2 ** 3))  # String repetition with exponentiation

my_float = 2.5 * 2
print("Hello " * int(my_float))  # String repetition with float conversion

### Comparison Operators ###

# Operations with integers
print(3 > 4)  # Greater than
print(3 < 4)  # Less than
print(3 >= 4)  # Greater than or equal to
print(4 <= 4)  # Less than or equal to
print(3 == 4)  # Equal to
print(3 != 4)  # Not equal to

# Operations with strings
print("Hello" > "Python")  # Lexicographical comparison
print("Hello" < "Python")
print("aaaa" >= "abaa")  # Lexicographical comparison (ASCII order)
print(len("aaaa") >= len("abaa"))  # Length comparison
print("Hello" <= "Python")
print("Hello" == "Hello")
print("Hello" != "Python")

### Logical Operators ###

# Based on Boolean Algebra https://en.wikipedia.org/wiki/Boolean_algebra
print(3 > 4 and "Hello" > "Python")  # Logical AND
print(3 > 4 or "Hello" > "Python")  # Logical OR
print(3 < 4 and "Hello" < "Python")  # Logical AND
print(3 < 4 or "Hello" > "Python")  # Logical OR
print(3 < 4 or ("Hello" > "Python" and 4 == 4))  # Complex logical expression
print(not(3 > 4))  # Logical NOT
