# Encapsulation: It is nothing but binding the data into a single class and controlling the access (data means variables and methids)
class Student: 
# to declare and initialize the variables 
    def __init__(self): 
        self.id = 10 
        self.name = 'Raju' 
# display students details 
    def display(self): 
        print(self.id) 
        print(self.name)

# note:special method def __init__(self) is to declare and initialize the instance variables of a class
