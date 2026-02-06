# 5 types of inheritances 1.Single inheritance 2.Multilevel Inheritance 3.Multiple Inheritance 4.Hierarchical Inheritance 5.Hybrid Inheritance

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
    