"""
    __call__ is a special function attribute on the class which enables the instance object callable like a function. This is useful when needing a function which maintains state between calls and optionally needs to support attributes or methods to query and modify that state.

    functions are a special callable objects!


    def simply binds the function body to a function name which becomes an object; def is only executed at runtime. 
    
    Local functions are also executed at runtime and each separate outer function call will create a new local function object. Local functions are simply objects created with the outer function scope but it has no relation to the outer function itself. It follows the LEGB rule and any variables used within local function are searched from itself, outer function and global scope. 
    Local functions are useful for specialized, one-off functions, aidding for code organisation and readability. Unlike lambda, it can contain multiple statements and expressions. 

    Local functions can use and bind objects that're no longer exist through closure which essentailly remembers the objects from the enclosing scope that the local function needs. It effectively prevent those object being garbage collected. If a function closes over any objects, the net function has __closure__ attribute which maintains.


    Decorators are callable objects that take in a callable and returns a callable. Decorators can modify or enhance functions without changing their definition.  
"""

import socket
class Resolver:

    def __init__(self):
        self._cache = {}
    

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]


    def clear(self):
        self._cache.clear()
    

    def has_host(self, host):
        return host in self._cache


def sort_with_local(strings):
    def last_letter(s):
        return s[-1]
    return sorted(strings.split(), key = last_letter)

def main():
     resolver = Resolver()
     # the instance object is callable due to __call__ definition
     #print(resolver('pluralsight.com'))

     # local function
     print(sort_with_local("hello from local function"))

     #closure demo
     inner = simple_closure()
     print(inner())
     print(inner.__closure__)

     # function factories using closure
     square = raise_to(2)
     print(square(4), square(25))

     cube = raise_to(3)
     print(cube(10), cube(1234))


     # useage of nonlocal
     t1 = make_timer()
     #print(t1())
     #print(t1())



     # a simple decorator
     print(simple_fun(5))    

def simple_closure():
    x = 'closed over'
    def inner():
        print(x)
    return inner


def raise_to(exp):
    return lambda x: pow(x,exp)


# use nonlocal to bind local variable to enclosing variable
import time
def make_timer():
    last_call = None
    def elapsed():
        nonlocal last_call
        now = time.time()
        if last_call is None:
            last_call = now
            return None
        result = now - last_call
        last_call = now
        return result
    return elapsed


# decorators creates a function object with the decorated function and pass it to the decorator function then returns a new function object which is bounded back to the decorated function!  
def simple_decorator(fun):
    return lambda  x : fun(x) + 2 

@simple_decorator
def simple_fun(x):
    return x + 3


# class as a decorator
class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0
    

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print('hello {}'.format(name))



if __name__ == '__main__':
    main()