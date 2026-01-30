# Class methods are the methods which act on the class variables or static variables
# @classmethod decorator above them. By default, the first parameter for class methods is ‘cls’ which refers to the class itself
# understanding class methods 
class Bird: 
# this is a class var 
    wings = 2     
# this is a class method 
    @classmethod 
    def fly(cls, name): 
        print("{} flies with {} wings".format(name, cls.wings)) 
    # display information for 2 birds 
Bird.fly("Sparrow") 
Bird.fly("Pigeon") 