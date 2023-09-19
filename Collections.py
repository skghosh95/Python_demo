Collections
# The collections module in Python implements specialized container datatypes providing alternatives to Python’s general purpose
# built-in containers, dict, list, set, and tuple.


Counter
# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

from collections import Counter
a = "aaaaabbbbcccdde"
my_counter = Counter(a)
print(my_counter)

print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

my_list = [0, 1, 0, 1, 2, 1, 1, 3, 2, 3, 2, 4]
my_counter = Counter(my_list)
print(my_counter)

# most common items
print(my_counter.most_common(1))

# Return an iterator over elements repeating each as many times as its count. 
# Elements are returned in arbitrary order.
print(list(my_counter.elements()))

Output: Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})
        dict_items([('a', 5), ('b', 4), ('c', 3), ('d', 2), ('e', 1)])
        dict_keys(['a', 'b', 'c', 'd', 'e'])
        dict_values([5, 4, 3, 2, 1])

        Counter({1: 4, 2: 3, 0: 2, 3: 2, 4: 1})
        [(1, 4)]
        [0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 4]


namedtuple
# namedtuples are easy to create, lightweight object types.

from collections import namedtuple
# create a namedtuple with its class name as string and its fields as string
# fields have to be separated by comma or space in the given string
Point = namedtuple('Point','x, y')
pt = Point(1, -4)
print(pt)

Person = namedtuple('Person','name, age')
friend = Person(name='Tom', age=25)
print(friend.name, friend.age)

Output: Point(x=1, y=-4)
        Tom 25

OrderedDict
# OrderedDicts are just like regular dictionaries but they remember the order that items were inserted. 
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(ordered_dict)

Output: OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])


defaultdict
# The defaultdict is a container that's similar to the usual dict container, but the only difference is that a defaultdict 
# will have a default value if that key has not been set yet.
from collections import defaultdict

# initialize with a default integer value, i.e 0
d = defaultdict(int)
d['yellow'] = 1
d['blue'] = 2
print(d.items())
print(d['green'])

Output: dict_items([('yellow', 1), ('blue', 2)])
        0

# initialize with a default list value, i.e an empty list
d = defaultdict(list)
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 5)]
for k, v in s:
    d[k].append(v)

print(d.items())
print(d['green'])
Output: dict_items([('yellow', [1, 3]), ('blue', [2, 4]), ('red', [5])])
[]


deque
#A deque is a double-ended queue. It can be used to add or remove elements from both ends.

from collections import deque
d = deque()

# append() : add elements to the right end 
d.append('a')
d.append('b')
print(d)

# appendleft() : add elements to the left end 
d.appendleft('c')
print(d)

# pop() : return and remove elements from the right
print(d.pop())
print(d)

# popleft() : return and remove elements from the left
print(d.popleft())
print(d)

# clear() : remove all elements
d.clear()
print(d)

d = deque(['a', 'b', 'c', 'd'])

# extend at right or left side
d.extend(['e', 'f', 'g'])
d.extendleft(['h', 'i', 'j']) # note that 'j' is now at the left most position
print(d)

# count(x) : returns the number of found elements
print(d.count('h'))

# rotate 1 positions to the right
d.rotate(1)
print(d)

# rotate 2 positions to the left
d.rotate(-2)
print(d)


Output:
deque(['a', 'b'])
deque(['c', 'a', 'b'])
b
deque(['c', 'a'])
c
deque(['a'])
deque([])
deque(['j', 'i', 'h', 'a', 'b', 'c', 'd', 'e', 'f', 'g'])
1
deque(['g', 'j', 'i', 'h', 'a', 'b', 'c', 'd', 'e', 'f'])
deque(['i', 'h', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'j'])

