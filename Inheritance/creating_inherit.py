
# sub class acquiring properties of base class
# Inheritance allows a class to reuse the attributes and methods of another class, reducing code duplication and improving maintainability.

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
