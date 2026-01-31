# Creating another class within a class is called inner class
# inner class example 

print("using Method 1")
# Creating instance for inner class method 1
class Person: 
    def __init__(self): 
        self.name = 'Charles'   
        self.db = self.Dob() 
 
    def display(self): 
        print('Name= ', self.name)         
 
    # this is inner class 
    class Dob: 
        def __init__(self): 
            self.dd = 10 
            self.mm = 5 
            self.yy = 1988 
        def display(self): 
            print('Dob= {}/{}/{}'.format(self.dd, self.mm, self.yy)) 
 
# creating Person class object  
p = Person() 
p.display() 
 
# create inner class object 
x = p.db 
x.display() 


print("using Method 2")

# creating instance for inner class method 2
# inner class example 
class Person: 
    def __init__(self): 
        self.name = 'Charles'    
 
    def display(self): 
        print('Name= ', self.name)         
 
    # this is inner class 
    class Dob: 
        def __init__(self): 
            self.dd = 10 
            self.mm = 5 
            self.yy = 1988 
        def display(self): 
            print('Dob= {}/{}/{}'.format(self.dd, self.mm, self.yy)) 
 
# creating Person class object  
p = Person() 
p.display() 
 
# create inner class object 
x = Person().Dob()
x.display() 