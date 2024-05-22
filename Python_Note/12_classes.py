### Classes ###

# Definition

class MyEmptyPerson:
    pass  # To be able to leave the class empty

print(MyEmptyPerson)  # Prints the class itself
print(MyEmptyPerson())  # Prints an instance of the class

# Class with constructor, functions, and private and public properties

class Person:
    def __init__(self, name, surname, alias="No alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Public property
        self.__name = name  # Private property

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} is walking")

my_person = Person("Brais", "Moure")
print(my_person.full_name)  # Prints the full name of the person
print(my_person.get_name())  # Prints the private name of the person
my_person.walk()  # Prints that the person is walking

my_other_person = Person("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)  # Prints the full name of the other person
my_other_person.walk()  # Prints that the other person is walking
my_other_person.full_name = "Héctor de León (The dog crazy)"
print(my_other_person.full_name)  # Prints the new full name of the other person

my_other_person.full_name = 666  # Attempting to set a non-string value to the full name
print(my_other_person.full_name)  # Prints the new full name of the other person, which is now an integer
