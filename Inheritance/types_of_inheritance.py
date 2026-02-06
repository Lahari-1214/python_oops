# 5 types of inheritances 1.Single inheritance 2.Multiple Inheritance 3.Multilevel Inheritance  4.Hierarchical Inheritance 5.Hybrid Inheritance

# Single inheritance:Deriving one or more sub classes from a single base class is called ‘single inheritance’.
class Bank(object):
    cash = 100000000 
    @classmethod
    def available_cash(cls):
        print(cls.cash)

class AndhraBank(Bank):
    pass

class Statebank(Bank):
    cash = 200000000
    @classmethod
    def available_cash(cls):
        print("statebank")
        print(cls.cash+Bank.cash)

a = AndhraBank()
a.available_cash()

s = Statebank()
s.available_cash()
    


# Multiple Inheritance:Deriving sub classes from multiple (or more than one) base classes is called ‘multiple inheritance’. 
# Syntax:class Subclass(Baseclass1, Baseclass2, … ): 

class Father: 
    def height(self): 
        print('Height is 6.0 foot') 
 
class Mother: 
    def color(self): 
        print('Color is brown') 
 
class Child(Father, Mother): 
    pass 
 
c = Child() 
print('Child\'s inherited qualities: ') 
c.height() 
c.color() 

# problems of using multiple inheritance: all the constructors of super class doesn't available to the sub class for the purpose we have Method Resolution order (MRO) which is described in MRO.py



