from sorted_set import SortedSet
from random import randrange
from pprint import pprint as pp
from timeit import timeit

# create a SortedSet with 2000 elements within range between [0, 1000)
s = SortedSet(randrange(1000) for _ in range(2000))

# a dict for checking which element is in the SortedSet
inset_dict = {i : i in s for i in range(1000)}

# another way of checking whether the element is in the set using count
inset_dict2 = {i : s.count(i) == 1 for i in range(1000)}
#pp(inset_dict2)
print(timeit(stmt="[s.count(i) for i in range(1000)]", number = 100, setup="from __main__ import s"))