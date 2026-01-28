# Creating new classes from existing class, that means the new class acquire all the properties of the parent class is said to be inheritance
# Creating class B from class A 
class A :     
    a = 1 
    b = 2 
    def method(cls):
        print(cls.a)
        print(cls.b)
        print("Method of A")
class B(A):
    c = 3
    def method2(cls):
        print("Method of B")
        print(cls.c)

# now B can access all the members present in A

b = B()
b.method2()
b.method()