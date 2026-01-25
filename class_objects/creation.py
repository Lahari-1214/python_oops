"""
Features of Object Oriented Programming System (OOPS) 
There are five important features related to Object Oriented Programming System. They 
are: 
 Classes and objects 
 Encapsulation 
 Abstraction 
 Inheritance 
 Polymorphism
"""

# object Definition: An object is anything that really exists in the world and can be distinguished from others.
# Every object has some behavior. The behavior of an object is represented by attributes and actions. 

# class Definition: A class is a model or blueprint for creating objects
#  A class and its objects are almost the same with the difference that a class does not exist physically, while an object does


# let's create a class
# A class is created by using the keyword, class. 

# This is a class
class Person:
    # These are attribute
    name = 'Leela'
    age = 21
    # action means function : inside the class it will be called as method
    def talk(cls):
        print(cls.name)
        print(cls.age)

# when we want to use the class then we have to create object
p1 = Person()
p1.talk()

# Here, p1 is an object of Person class. Object represents memory to store the actual data. The memory needed to create p1 object is provided by PVM. cls’ represents a default parameter that indicates the class.

