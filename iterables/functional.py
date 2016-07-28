#### functionaly style Python ###

# map returns a lazy map object by iterating each item in the given sequence in order 
codepoints = map(ord, "The quick jump brown fox")
print(list(codepoints))


class Trace:
    def __init__(self):
        self.enabled = True
    

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print("Calling {}".format(f))
            return f(*args, **kwargs)
        return wrap

### class is callable and Trace() returns a callable which calls on ord retruning another callable 
tracedOrds = map(Trace()(ord), "The quick brown fox")
for o in tracedOrds:
    print(o)


# map can take as mnay inputs as needed for the passed in function and some sequences can have infinite sizes; map will terminate as soon as any sequence is terminated. 

# this results a collection of only 5 items. 
simple_sum = map(lambda x, y, z: x + y + z, range(5), range(1, 7), range(2, 9))
print(list(simple_sum))


# map and comprehension can be used for the same task depending on personal preference
l1 = [str(i) for i in range(5)]
l2 = map(str, range(5))


# map and filter in Python2 return list rather than lazy iterable objects. 

# filter only takes one input sequence and one function returning a lazy collection with all elements that are true from the given function
positives = filter(lambda x: x > 0, [0, 4, -1, 4, -59, 23, True]) # note that True = 1 > 0
print(list(positives))

# passing None, means only elements in the sequence is truy is returned; 
trues = filter(None, [False, 1, 0, True, [], [23, 4]]) # 0 is falsy
print(list(trues))


from functools import reduce
import operator
# reduce() repeatedly applies a function to elements of a sequence reducing to a single element.
# it optionally takes a seed value which defaults to the 1st element. 
# it's called aggregate in LINQ and fold in other functional language
poor_man_sum = reduce(operator.add, [1, 2, 3,4 , 5], -15)
print(poor_man_sum)

# if the passed in function takes two arguments, it will first pass in the 1st element then 2nd element ... until it statisfies the function argument requirment then run the function and use the return result as the 1st argument in the second round
def mul(x, y):
    print("mul {} {}".format(x, y))
    return x * y 
poor_sum2 = reduce(mul, range(1, 10))
print(poor_sum2)

# a few edge cases:
    # passing an empty sequence throws a type error 
    # passing a sequence of single element; that element is returd without ever calling reduce 




""" Iteration protocols:

An iterable object is simply object that responds to the iter() function, i.e. an object implementes __iter__(). iter() method is required to return an iterator object.

An iterator object which implements the iterable protocol e.g. implementing the iter() and generally speaking iterator object's iter method just returns itself though not always the case.
Iterator object also needs to implement __next__() which either returns the next element in the sequence or raise a StopIteration exception.
"""

class SimpleIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            res = self.data[self.index]
            self.index += 1
            return res 
        else:
            raise StopIteration()

class SimpleIteratable:
    def __init__(self, data):
        self.data = data

    # iterable object needs to return iterator object on the iter()!!!!    
    def __iter__(self):
        return SimpleIterator(self.data)

si = SimpleIteratable([1,2,3])
for i in si:
    print(i)


class AlternativeIteration:
    def __init__(self, data):
        self.data = data

    # this also enables iteration/for loop 
    def __getitem__(self, index):
        return self.data[index]

ai = AlternativeIteration([1, 2, 3])
for i in ai:
    print(i)


######## extended iter(): iter(callable, sentinel); callable must take 0 argument
#### iteration stops when callable produces this sentinel value. It's often used to create inifite sequence from existing functions
from datetime import datetime as dt
timestamp = iter(dt.now, None) # this creates an infinite sequence 
print(next(timestamp))
print(next(timestamp)) 

## another common use is end reading a file when some text is read
# for line in iter(lambda f.readline().strip(): 'END'):
#     print line ## this will end when a line is END is read.
