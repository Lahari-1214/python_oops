# Hiding the unnecessary data from the user and expose only that data that is of interest to the user is called abstraction
class Myclass: 
# this is constructor. 
    def __init__(self):           
        self.__y = 3   # this is private variable
m = Myclass() 
# print(m.y)   # error 

# name mangling: 
#   In name mangling, we have to use one underscore before the classname and two underscores after the classname. Like this, using the names differently to access the private variables is called name mangling
print(m._Myclass__y)

class Myclass2:
    def __init__(self):
        self.__c = 34
        self.d = 30
    def print(self):
        print(self.d)

m1 = Myclass2()
print(m1.d)
print(m1._Myclass2__c)


