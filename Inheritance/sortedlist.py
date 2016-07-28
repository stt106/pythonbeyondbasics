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

######### Multiple inheritance 
class SortedIntList(IntList, SortedList):
    def __repr__(self):
        return "SortedIntList({!r})".format(list(self))


# if subclass does not define init() then only the first base class init() will be called
sil = SortedIntList([3, 4, 2, 5])
# this returns a tuple of base classes of the same order listed in the class definition
print(SortedIntList.__bases__) 
print(IntList.__bases__) # single inheritance has __base__ and __bases__ (single item tuple)


# MRO: Method Resolution Order determines which method should be invoked if multiple inheritance 
# base classes both define the same class. The MRO graph starts with the subclass -> first base class-> second base class -> base class of first base class -> base class of 2nd base class ->... -> object (the base class of everything!)
# MRO is calculated using C3; perserve the subclass-baseclass order. 

print(SortedIntList.__mro__) # a tuple of MRO
print(SortedIntList.mro()) # a list of MRO
