# Passing members of one class to another class
# this class contains employee details 
class Emp: 
    # this is a constructor. 
    def __init__(self, id, name, salary):           
        self.id = id 
        self.name = name 
        self.salary = salary 
 
    # this is an instance method. 
    def display(self):           
        print('Id=', self.id)  
        print('Name=', self.name) 
        print('Salary= ', self.salary) 
 
# this class displays employee details 
class Myclass: 
    # method to receive Emp class instance 
    # and display employee details 
    @staticmethod 
    def mymethod(e): 
        # increment salary of e by 1000 
        e.salary+=1000; 
        e.display() 
 
# create Emp class instance e 
e = Emp(10, 'Leela', 15000.75) 
# call static method of Myclass and pass e 
Myclass.mymethod(e) 