
# sub class acquiring properties of base class
# Inheritance allows a class to reuse the attributes and methods of another class, reducing code duplication and improving maintainability.
#  syntax: class Subclass(Baseclass):  

class Animal:        # Parent class
    def sound(self):
        print("Animals make sound")

class Dog(Animal):   # Child class
    def bark(self):
        print("Dog barks")

d = Dog()
d.sound()   # inherited method
d.bark()

# Benefits: code reusablity, cleaner code,Easy maintance

# The next question is why the base class members are automatically available to sub class? 
# When a child class inherits from a parent class, it automatically gains access to all public and protected members (attributes and methods) of the parent class. This is because the child class is essentially an extension of the parent class, inheriting its structure and behavior.