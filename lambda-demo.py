"""
lambda is an expression which evaluates to a function 
"""

people = ["Ben Li", "Andy", "Ning", "Pat", "Rita", "Jacky"]
sortedPeople = sorted(people, key = lambda name : name[-1])
print(sortedPeople)

# lambda with two arguments 
add = lambda x, y : x + y 
print(add(30, 40))

is_odd = lambda x: x & 1 == 1
print(is_odd(4))
print(callable(is_odd)) # use built-in callable to check whether something is callable.
print(callable(add))


"""
Extend format argument syntax applies to functions, lambda, other callables:

   1. positional arguments is achieved through *args which retruns a tuple
"""

# using a regular positional argument here is better than using try except block of a key positional *args argument only. Because it will raise a more meaningful exception when no arguments is passed in. This is helpful when there is a lower bound in the positional *args.
def hypervolume(length, *args):
    v = length
    for length in args:
        v *= length
    return v

print(hypervolume(3))
print(hypervolume(3, 4))
print(hypervolume(3, 4, 5))


# any number of keyword arguments using **kwargs. 
def tag(name, **kwargs):
    result = '<' + name
    for k, v in kwargs.items():
        result += ' {key} = "{value}"'.format(key = k, value = str(v))
    result += '/>'
    return result

print(tag('img', src="monet.jpg", alt="Sunrise by Calude Monet", border=1))

# combine *args and **kwargs; # extend call syntax using iterable series s.a. tuples to populate positional arguments and mapping types s.a. dict to populate keyword arguments. 

def print_args(p1, p2, *args, k1, k2, **kwargs):
    print(p1)
    print(p2)
    print(args)
    print(k1)
    print(k2)
    print(kwargs)

print_args(1, 2, 3, 4, k1 = 'key argument 1', k2 = 'key argument 2', ko1 = 'optional key argument 1')


# using *tuple to instruct a tuple unpacking to create the positional arguments.
# using ** to instructe a dict mapping to the keyword arguments.  
print_args(*(1, 2, 3, 4), k1 = 'k1', k2 = 'k2', **dict(key1 = 1, key2 = 2))

# one usage of argument extension is forwarding the arguments 
def trace(f, *args, **kwargs):
    print("args= ", args)
    print("kwargs= ", kwargs)
    result = f(*args, **kwargs)
    print("result =", result)
    return result 

# must pass the **kwargs using keyword argument 
trace(int, "1000", base = 2)

if __name__ == '__main__':
    # zip * idiom is an important technique to do transposition.
    sunday = [10, 12, 24, 5, 7, 62]
    monday = [14, 21, 49, 52, 1, 19]
    tuesday = [3, 25, 2, 3, 5, 69]
    days = [sunday, monday, tuesday]
    transform = list(zip(*days))
    from pprint import pprint as pp
    pp(transform)




