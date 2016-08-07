"""
Each collection protocol is founded on the idea of implementing a specific set of methods, usually
"""

# issubclass(c1, c2) can check whether class c1 is a subclass of another class c2 using duck typing e.g. when c1 is not directly derived
# from c2 but it still implementes the same protocol as c2 then issubclass(c1, c2) will return true. 


# subclass from the Sequence module on the collections.abc to provide contains, iter, reversed, index and count once len and iter ArithmeticError
# implemented.
from collections.abc import Sequence, Set
from bisect import bisect_left
from itertools import chain 


class SortedSet(Sequence, Set): # it's recommended to subclass from Sequence for a custom collection type.
    def __init__(self, items=None):
        # by convention a default collection takes no argument and creates an empty collection
        # use set ctor here to eliminate duplicates 
        self._items = sorted(set(items)) if items is not None else []

    # container protocol; executed through in/not in
    def __contains__(self, item):
        # this takes O(n)
        #return item in self._items

        # this takes O(logn)
        # index = bisect_left(self._items, item)
        # return (index < len(self._items)) and (self._items[index] == item) 

        # use index protocol to implement contains protocol to avoid duplication
        try:
            self.index(item)
            return True
        except ValueError:
            return False
    
    # size protocol; if __reversed__() is not implemented explicitly it will fallback to __len__ and __iter__ implicitly.
    def __len__(self):
        return len(self._items)
    
    #iter protocol is normally either delegated to the iter of the underlying collection or implemented using a generator 
    def __iter__(self):
        ##### use a generator to implement the iter protocol
        # for i in self._items:
        #     yield i
        return iter(self._items)


    # sequence protocol; index can be a slice object which accepts(start, stop, step)
    def __getitem__(self, index):
        result = self._items[index]
        # either accept slice object or a single indexer 
        return SortedSet(result) if isinstance(index, slice) else result

    
    # default count() is O(n); for SortedSet O(logn) is possible
    def __count__(self, item):
        # using the contains protocol to implement the count protocol
         return int(item in self._items) # change a bool to 0 or 1

    
    # default index implementation is O(n); using binary search it can get O(logn)
    def index(self, item):
        index = bisect_left(self._items, item)
        if index < len(self._items) and (item == self._items[index]):
            return index
        raise ValueError("{} not found".format(item))


    # for a full implementation of sequence protocol; also implement concentantion and repetition
    def __add__(self, other):
        return SortedSet(chain(self._items, other._items)) # stream elements from each iterable until it's both exhausted

    # left multiplication
    def __mul__(self, factor):
        return SortedSet() if factor < 1 else self

    
    def __rmul__(self, factor):
        return self * factor # delegate to __mul__

    # equality protocol; by default == tests identity rather than value equality; many built in collection override the __eq__ to provide value equality
    # on == which is used on assert.areEqual()
    def __eq__(self, other):
        # python runtime will retry the comparison once with the arguments reversed potentially giving a different implementation of 
        #eq on another object the chance to respond.
        if not isinstance(other, SortedSet):
            return NotImplemented # NOTE here return the NotImplemented object not raise the NotImplementedError
        return self._items == other._items
    
    def __ne__(self, other):
        if not isinstance(other, SortedSet):
            return NotImplemented
        return self._items != other._items


    def __repr__(self):
        return "SortedSet({})".format(repr(self._items) if self._items else '')


    # set protocol operations; implementing the methods to allow any iterable; if implementing the operator symbols it must take the same type of two objects instances. 
    def issubset(self, iterable):
        return self <= SortedSet(iterable)

    def issuperset(self, iterable):
        return self >= iterable
    
    def intersection(self, iterable):
        return self._items & iterable
    
    def union(self, iterable):
        return self._items | SortedSet(iterable)
    
    def symmetric_difference(self, iterable):
        return self._items ^ SortedSet(iterable)
    
    def difference(self, iterable):
        return self._items - SortedSet(iterable) 

    
     