# step 1: A class is created with the class keyword followed by classname
# step 2: After the classname object is written inside the Classname

# note:object represents the base class name from where all classes in python are derived Even our own classes are also derived from object class.
class Student:     
# another way is: class Student(object):  
# the below block defines attributes 
    def __init__(self):           
        self.name = "Leela" 
        self.age = 20 
        self.marks = 900 
    # the below block defines a method 
    def talk(self):           
        print("Hii myname is:", self.name)  
        print("My age is:", self.age) 
        print("My score:", self.marks) 