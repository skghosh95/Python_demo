Itertools
# The Python itertools module is a collection of tools for handling iterators. Simply put, iterators are data types that can be used in a for loop. The most common iterator in Python is the list.

product()
# This tool computes the cartesian product of input iterables.
from itertools import product

prod = product([1, 2], [3, 4])
print(list(prod)) # note that we convert the iterator to a list for printing

Output:
[(1, 3), (1, 4), (2, 3), (2, 4)]
