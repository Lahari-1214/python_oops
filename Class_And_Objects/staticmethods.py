#  Static methods are used when some processing is related to the class but does not need the class or its instances to perform any work
#  Static methods are written with a decorator @staticmethod
# understanding static methods
class Myclass:
    # this is a class or static
    n = 0
    def __init__(self):
        Myclass.n = Myclass.n+1

    @staticmethod
    def noObj():
           print("No of objects created",Myclass.n)

obj1 = Myclass()
obj2 = Myclass()
obj3 = Myclass()
obj4 = Myclass()
Myclass.noObj()