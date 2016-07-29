"""
Two string representations:
    1) repr: produce an unambiguous string representation of an object hence it should include the type of the object along with any identifying fields. Sometimes people think the result of repr should be able to replicate the object instance (not always feasible). 

        1.2) Exectness is more important than human-friendliness / more information than str 
       Suited for debugging  hence ideally for developer!
       Includes identifying information
       Generally best for logging

        1.3) It's good practice to always override the default implementation of repr'

    2) str produces a readable, human-friendly representation of an object; not programmer oriented.

    Where are they used?
        print() uses str() which internally simply calls repr()!
        repr() is used when showing elements of a collection
        format() calls str.__format__() and default implementation of __format__() calls str(); can force format to use repr by specifying a format of {!r}

    sometimes repr() should be shorter than str() depending on the situation.

    3) ascii() replaces non-ASCII characters with escape sequences which can be useful where need to serialize data as ascii or if you can't communicate encoding information but you don't want to lose Unicode data.
      ord() converts a unicode endpoint to an integer and chr() converts an integer back to a unicode endpoint. 
"""

"""
standard library module reprlib supports alternative implementations of repr(); the primary feature is it places limits on how large a string can be, which is useful for large collections. reprlib.repr() prints only a few of a very large collection.
"""

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    

    def __repr__(self):
        return "Point2D (X = {}, Y = {})".format(self.x, self.y)


def test_two_representation():
    p = Point2D(20, 34)
    print(str(p)) # the same as print(p)
    print(p)
    print(repr(p))

    points = [Point2D(i, i + 3) for i in range(3)] # use comprehension to create a list of Point2D
    print(points) # this uses repr() for each element rather than str 

    print("this is a {!r}".format(p)) # force to use repr format 
    print("this is a point {!s}".format(p)) # force to use str which is the default


import reprlib
def test_reprlib():
    many_points = [Point2D(x, y) for x in range(1000) for y in range(1000)] # this is 1000*1000 = 1M points list 
    print(reprlib.repr(many_points))



def main():
    test_two_representation()
    test_reprlib()

if __name__ == '__main__':
    main()
