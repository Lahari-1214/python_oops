# Types of methods: 1.Instance methods a)Accessor methods b)mutator methods 2.class methods 3.static methods

# Instance Methods
# instance methods to process data of the objects 
class Student:      
# this is a constructor. 
    def __init__(self, n = ' ', m=0):           
        self.name = n 
        self.marks = m 
    # this is an instance method. 
    def display(self):           
        print('Hi', self.name)  
        print('Your marks', self.marks) 
    # to calculate grades based on marks. 
    def calculate(self): 
        if(self.marks>=600): 
            print('You got first grade')
        elif(self.marks>=500): 
            print('You got second grade') 
        elif(self.marks>=350): 
            print('You got third grade') 
        else:  
            print('You are failed') 
 
# create instances with some data from keyboard 
n = int(input('How many students? ')) 
 
i=0 
while(i<n): 
    name = input('Enter name: ') 
    marks = int(input('Enter marks: ')) 
 
    # create Student class instance and store data 
    s = Student(name, marks) 
    s.display() 
    s.calculate() 
    i+=1 
    print('---------------------') 

# Accessor methods: These methods are used to access the data members of a class. They do not modify the data members.(getter method)
# Mutator methods: These methods are used to modify the data members of a class. They allow controlled access to the data members.(setter method)

    