"""
1. Subclass doesn't auto call base class __init__(). If subclass doesn't fine init() then base class init() will be called when a subclass instance is initialised.

"""

class Base():
    def __init__(self):
        print('Base initialiser')
    
    def f(self):
        print("Base.f()")

class Sub(Base):
    def f(self):
        print("Sub.f()") # override the base class 


class Sub2(Base):
    def __init__(self): # override base init
        #super().__init__() have to call this explicitly.
        print("Subs initialiser doesnot auto call base initialiser when overriding it")

sub = Sub() # this will auto call base init() if Sub doesn't have an init()
sub.f()

sub2 = Sub2()
