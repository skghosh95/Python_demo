The random module
# This module implements pseudo-random number generators for various distributions. 

import random

# random float in [0,1)
a = random.random()
print(a)

# random float in range [a,b]
a = random.uniform(1,10)
print(a)

# random integer in range [a,b]. b is included
a = random.randint(1,10)
print(a)

# random integer in range [a,b). b is excluded
a = random.randrange(1,10)
print(a)

# random float from a normal distribution with mu and sigma
a = random.normalvariate(0, 1)
print(a)

# choose a random element from a sequence
a = random.choice(list("ABCDEFGHI"))
print(a)

# choose k unique random elements from a sequence
a = random.sample(list("ABCDEFGHI"), 3)
print(a)

# choose k elements with replacement, and return k sized list
a = random.choices(list("ABCDEFGHI"),k=3)
print(a)

# shuffle list in place
a = list("ABCDEFGHI")
random.shuffle(a)
print(a)

Output:
0.8125522008601908
5.211197733637115
9
3
-1.0370265833885448
D
['E', 'F', 'H']
['I', 'G', 'C']
['I', 'A', 'H', 'D', 'G', 'E', 'B', 'C', 'F']










