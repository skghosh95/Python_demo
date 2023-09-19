Lambda functions
# A lambda function is a small (one line) anonymous function that is defined without a name. A lambda function can take any number of arguments, but can only have one expression.

# a lambda function that adds 10 to the input argument
f = lambda x: x+10
val1 = f(5)
val2 = f(100)
print(val1, val2)

# a lambda function that multiplies two input arguments and returns the result
f = lambda x,y: x*y
val3 = f(2,10)
val4 = f(7,5)
print(val3, val4)

Output:
15 110
20 35

Usage example: Lamdba inside another function
# Return a customized lambda function from another function and create different function variations depending on your needs.

def myfunc(n):
    return lambda x: x * n

doubler = myfunc(2)
print(doubler(6))

tripler = myfunc(3)
print(tripler(6))

Output:
12
18



Custom sorting using a lambda function as key parameter
# The key function transforms each element before sorting.

points2D = [(1, 9), (4, 1), (5, -3), (10, 2)]
sorted_by_x = sorted(points2D)
print(sorted_by_x)

#sorted by y axis
sorted_by_y = sorted(points2D, key= lambda x: x[1])
print(sorted_by_y)

#sorted by sum
sorted_by_sum = sorted(points2D, key= lambda x: x[0] + x[1])
print(sorted_by_sum)

Output:
[(1, 9), (4, 1), (5, -3), (10, 2)]
[(5, -3), (4, 1), (10, 2), (1, 9)]
[(5, -3), (4, 1), (1, 9), (10, 2)]


Use lambda for map function
# map(func, seq), transforms each element with the function.
a  = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x * 2 , a)

# However, try to prefer list comprehension
# Use map if you have an already defined function
c = [x*2 for x in a]
print(list(b))
print(c)

Output:
[2, 4, 6, 8, 10, 12]
[2, 4, 6, 8, 10, 12]


Use lambda for filter function
# filter(func, seq), returns all elements for which func evaluates to True.

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = list(filter(lambda x: (x%2 == 0) , a))

# However, the same can be achieved with list comprehension
c = [x for x in a if x%2 == 0]
print(b)
print(c)

Output:
[2, 4, 6, 8]
[2, 4, 6, 8]


reduce
# reduce(func, seq), repeatedly applies the func to the elements and returns a single value.
# func takes 2 arguments.

from functools import reduce
a = [1, 2, 3, 4]
product_a = reduce(lambda x, y: x*y, a)
print(product_a)
sum_a = reduce(lambda x, y: x+y, a)
print(sum_a)

Output:
24
10







