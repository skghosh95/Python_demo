Generators
# A generator is defined like a normal function but with the yield statement instead of return.

def my_generator():
    yield 1
    yield 2
    yield 3


Execution of a generator function

def my_generator():
  for i in  range(5):
    yield i
gen = my_generator()
# print(next(gen))
for j in gen:
  print(j)

Output:
0
1
2
3
4
