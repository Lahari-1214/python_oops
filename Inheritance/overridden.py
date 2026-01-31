# If a child class has its own constructor, it does NOT automatically call the parent class constructor. {using super() we can call the parent class constructor}

'''
# When the programmer writes a constructor in the sub class, the super class constructor is not available to the sub class
#  In this case, only the sub class constructor is accessible from the sub class object. 
# That means the sub class constructor is replacing the super class constructor. This is called constructor overriding'''


''' Similarly in the sub class, if we 
write a method with exactly same name as that of super class method, it will override the 
super class method. This is called method overriding.'''

# overriding the base class constructor and method in sub class 
class Father: 
    def __init__(self): 
        self.property = 800000.00 
    def display_property(self): 
        print('Father\'s property= ', self.property) 
class Son(Father):     
    def __init__(self): 
        super().__init__()  # Call parent constructor
        self.property = 200000.00     
    def display_property(self): 
        print('Child\'s property= ', self.property) 
# create sub class instance and display father's property 
s = Son() 
s.display_property() 