class Student:      
# this is a special method called constructor. 
    def __init__(self):           
        self.name = 'Leela' 
        self.age = 20 
        self.marks = 900 
    # this is an instance method. 
    def talk(self):           
        print('Hi, I am', self.name)  
        print('My age is', self.age) 
        print('My marks are', self.marks) 

# creating object:
s1 = Student()

# 1)First of all, a block of memory is allocated on heap.
# 2)After allocating memory init method called internally
s1.talk()