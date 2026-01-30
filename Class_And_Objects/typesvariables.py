# There are 2 types of variables 1.Instance variables and 2. Class or static variables
# Instance variables are the variables whose separate copy is created in every instance (or object)
# instance vars example 
class Sample:      
    # this is a constructor. 
    def __init__(self):    
        self.x = 10         
 
    # this is an instance method. 
    def modify(self):           
        self.x+=1 
 
# create 2 instances 
s1 = Sample() 
s2 = Sample() 
print("x in s1= ", s1.x) 
print("x in s2= ", s2.x) 
 
# modify x in s1 
s1.modify() 
print("x in s1= ", s1.x) 
print("x in s2= ", s2.x)

#  class variables are the variables whose single copy is available to all the instances of the class
# If we modify the copy of class variable in an instance, it will modify all the copies in the other instances
# class vars or static vars example 
class Sample:      
    # this is a class var 
    x = 10 
 
    # this is a class method. 
    @classmethod 
    def modify(cls):           
        cls.x+=1 
 
# create 2 instances 
s1 = Sample() 
s2 = Sample() 
print("x in s1= ", s1.x) 
print("x in s2= ", s2.x) 
 
# modify x in s1 
s1.modify() 
print("x in s1= ", s1.x) 
print("x in s2= ", s2.x) 