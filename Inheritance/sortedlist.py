class SimpleList:
    def __init__(self, data):
        self._data = list(data)

    def add(self, value):
        self._data.append(value)
    
    def __getitem__(self, index):
        return self._data[index]

    def sort(self):
        self._data.sort()
    
    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return "SimpleList({!r})".format(self._data)


class SortedList(SimpleList):
    def __init__(self, data=()):
        #print('SortedList initialiser')
        super().__init__(data) # call base initialiser explicitly
        self.sort() # this is calling base class method but sorting the subclass instance 
    
    def add(self, value):
        super().add(value) # access base class implementation 
        self.sort() # always remain sorted in the sortedlist 
    
    def __repr__(self):
        return "SortedList({!r})".format(list(self))




sl = SortedList([4, 2, 1, -1, 49, 6])
print(sl)
sl.add(7)
print(sl)


###### isinstance(x, (T1, T2, ..)) checks whether x is of the same type Ti or any subtype of Ti;


class IntList(SimpleList):
    def __init__(self, items):
        for i in items:
            self._validateItem(i)
        # add items once they all pass the validation    
        super().__init__(items)


    @staticmethod
    def _validateItem(item): # NO instance self variable in the static method!
        if not isinstance(item, int):
            raise TypeError("IntList only supports integer value")
    
    def add(self, item):
        self._validateItem(item)
        super().add(item)
    
    def __repr__(self):
        return "IntList({!r})".format(list(self))
                
# checks direct or indirect inheritance; 
print(issubclass(IntList, SimpleList))
print(issubclass(IntList, IntList))

######### Multiple inheritance ###########
# the order of multiple base class matters (affect MRO);
class SortedIntList(IntList, SortedList):
    def __repr__(self):
        return "SortedIntList({!r})".format(list(self))


# if subclass does not define init() then only the first base class init() will be called
sil = SortedIntList([3, 4, 2, 5])
# this returns a tuple of base classes of the same order listed in the class definition
print(SortedIntList.__bases__) 
print(IntList.__bases__) # single inheritance has __base__ and __bases__ (single item tuple)


# MRO: Method Resolution Order determines which method should be invoked if multiple inheritance 
# base classes both define the same class. The MRO graph starts with the subclass itself -> first base class-> second base class -> base class of first base class -> base class of 2nd base class ->... -> object (the base class of everything!)
# MRO is calculated using C3; C3 perserves the subclass-baseclass order and the multiple base class order is also preserved. And first two qualities are preserved no matter where the class graph begins (relative class order is not important). The implementation of C3 is some inheritance decoration is not allowed (Python won't compile them!). For example class D(B, A, C): # if B, C both inherit from A this won't compile as B and C must be before A in the MRO.

# Python walks through the MRO list and call the method on the first object that defines the method.

print(SortedIntList.__mro__) # a tuple of MRO
print(SortedIntList.mro()) # a list of MRO
sil.add(1) # this calls the add on the IntList as it's the first object in the SortedIntList MRO defining add
print(sil)


########## How super() works? 
### Given a method resolution order and a class C, super() gives you an object which resolves methods using only part of the MRO that comes after C. In other words, super() doesn't work with the base classes of the class but instead it works with the MRO of the type of the object on which a method was originally invoked.
# super() actually returns a proxy object which routes methods calls if such method exist on the proxy. There're two types of super proxy: bound and unbounded. Bound proxy are bound to a specific instance or class objects.

# Unbound proxy are not bound to a class or instance in fact don't do any method dispatch themselves. It's a primary details for other python features and some prominent python developers consider them a bit of wart on the language.  

""" Bound proxy:
    class-bound proxy: super(base-class, derived-class); pass in two class objects and 2nd argument must be a subclass or the same as the first argument otherwise raise an exception.
    When resolving a method on the class-bound proxy, python first finds the MRO of the 2nd argument then take the first object after the 1st argument from the MRO list that defines the method. Note this the class-bound proxy is a class object not an instance object so it cannot invoke an instance method. 
"""
class_proxy = super(SortedList, SortedIntList)
print(type(class_proxy))
print(class_proxy)

""" Instance bound proxy bounds to an instance of the class:
    super(class, instance-of-class); 2nd argument must be an instance of the 1st class object or an instance of a class derived from the 1st argu.
    The resolution process:
        1) finds the MRO for the type of the second argument
        2) finds the location of the 1st argu in the MRO; this is always valid as the instance must be derived from the class. 
        3) take everything after that for resolving methods
    More importantly it bounds to an instance object and hence can be invoked directly on the instance. 
"""
instance_proxy = super(SortedList, sil)
print(SortedIntList.mro())
instance_proxy.add('this should not work but it does!')
print(sil)

better_instance_proxy = super(SortedIntList, sil)
try:
    better_instance_proxy.add('this is a better proxy!')
except TypeError as e:
    print(e)

""" Call super() without argument
    1) in an instance method, this is the same as super(class-of-method, self) and in a single inheritance it's equivalent to calling a method on the base class because the base class will be 1st one after the subclass on the subclass MRO.
    2) in a class method, it's the same as super(class-of-method, class); this again resolves to calling base class method in a single inheritance.
"""


""" How does add() work on SortedIntList
Because SortedIntList's MRO is [SortedIntList, IntList, SortedList, SimpeList, object], when call add() on an instance of SortedIntList e.g. sil
It firstly resolves to IntList.add() which also calls super() then it's using the same MRO of SortedIntList, so IntList.add() resolves to SortedList.add() which itself calls super() again and this time (just as IntList.add() it is also using MRO of SortedIntList) it's delegated to SimpleList.add(). They all use the same MRO of SortedIntList because super() on an instance method is the same as super(class-of-method, instance of the class) e.g. super(SortedIntList, sil) and because it's an instance method the sil instance is passed down through the inheritance herichy.

"""

'''
Objet is the ultimate base class of every object; it has some default implementation of some commonly used implementation details.
Because python is dynamic typed, no type safety check at compile time, inheritance is mostly used for sharing implementation rather than for ploymorsic behaviors achieved through inheritance in static typed languages. 
'''