# super() is a built-in method which is useful to call the super class constructor or methods from the sub class.

# super() can be used as:
'''
super().__init__()     
# call super class constructor 
super().__init__(arguments)# call super class constructor and pass  
# arguments  
super().method()  
 # call super class method 
''' 

# accessing base class constructor in sub class 
class Father: 
    def __init__(self, property=0): 
        self.property = property 
 
    def display_property(self): 
        print('Father\'s property= ', self.property) 
 
class Son(Father):     
    def __init__(self, property1=0, property=0): 
        super().__init__(property)    
        self.property1= property1  
 
    def display_property(self): 
        print('Total property of child= ', self.property1 + self.property) 
 
# create sub class instance and display father's property 
s = Son(200000.00, 800000.00) 
s.display_property() 


# few more additional examples of super() method
# Accessing base class constructor and method in the sub class 
class Square: 
    def __init__(self, x): 
        self.x = x 
 
    def area(self): 
        print('Area of square= ', self.x*self.x) 
 
class Rectangle(Square): 
    def __init__(self, x, y): 
        super().__init__(x) 
        self.y = y 

    def area(self): 
        super().area() 
        print('Area of rectangle= ', self.x*self.y) 
# find areas of square and rectangle 
a, b = [float(x) for x in input("Enter two measurements: ").split()] 
r = Rectangle(a,b) 
r.area() 