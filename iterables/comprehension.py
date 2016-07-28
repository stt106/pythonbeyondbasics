""" Comprehensions 
Shorthand syntax for creating collection and iterable objects

"""

### multiple inputs comprehensions ###
values = [x / (x - y)
            for x in range(100) if x > 50
            for y in range(100) if x - y != 0
        ]

# it's possible to refer the former clause in the latter clause
points = [(x, y) for x in range(10) for y in range(x)]
print(len(points))

### nested comprehensions
vals = [[y * 2 for y in range(x)] for x in range(10)]

# multiple and nested comprehensions apply to other collection types as well
unique_prodcuts = {x * y for x in range(10) for y in range(10)}

# generator comprehension
g = ((x, y) for x in range(10) for y in range(x))
