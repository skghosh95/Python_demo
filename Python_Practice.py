#Our First Python Program
print("Hello World")
# A Key Point to know about Python
# - It is a case sensitive language

# Variables
# Basic Types in Python - numbers(integers, floating), boolean, strings

# Example 1 :
name = "suman"
age = 22
print(name)
print(age)

#Example 2 :
name = "suman"
age = 22
name = "aman"
age = 24
print(name)
print(age)

#Example 3 :
first_name = "suman"
last_name = "ghosh"
age = 19
is_adult = True
print(first_name + " " + last_name)
print(age)
print(is_adult)

#> Exercise Solution
first_name = "Tony"
last_name = "Stark"
age = 52
is_genius = True
Taking Input
name = input("What is your name? ")
print("Hello " + name)
print("Welcome to our cool Python class")
> Exercise Solution
superhero = input("What is your superhero name? ")
print(superhero)
Type Conversion
old_age = input("Enter your age : ")
#new_age = old_age + 2
#print(new_age)
new_age = int(old_age) + 2
print(new_age)
#Useful converion functions
# 1. float()
# 2. bool()
# 3. str()
# 4. int()
> Code for Sum of 2 Numbers
first_number = input("Enter 1st number : ")
second_number = input("Enter 2nd number : ")
sum = float(first_number) + float(second_number)
print("the sum is : " + str(sum))
Strings
name = "Tony Stark"
print(name.upper())
print(name)
print(name.lower())
print(name)
print(name.find('y'))
print(name.find('Y'))
print(name.find("Stark"))
print(name.find("stark"))
print(name.replace("Tony Stark", "Ironman"))
print(name)
#to check if a character/string is part of the main string
print("Stark" in name)
print("S" in name)
print("s" in name)
Arithmetic Operators
print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print( 5 // 2)
print(5 % 2)
print(5 ** 2)
i = 5
i = i + 2
i += 2
i -= 2
i *= 2
Operator Precedence
result = 3 + 5 * 2 # 16 or 13 ?
print(result)
Comments
# This is a comment & useful for people reading your code
# This is another line
Comparison Operators
is_greater = 1 > 5
is_lesser = 1 < 5
# 1 <= 5
# 1 >= 5
is_not_equal = 1 != 5
is_equal = 1 == 5
Logical Operators
# or -> (atleast one is true)
# and -> (both are true)
# not -> (reverses any value)
number = 2
print(number > 3)
print(number < 3)
print(not number > 3)
print(not number < 3)
print(number > 3 and number > 1)
print(number > 3 or number > 1)
If statements
age = 13
if age >= 18:
print("you are an adult")
print("you can vote")
elif age < 3:
print("you are a child")
else:
print("you are in school")
print("thank you")
Let’s build a Calculator
#Our Calculator
first = input("Enter first number : ")
second = input("Enter second number : ")
first = int(first)
second = int(second)
print("----press keys for operator (+,-,*,/,%)----------")
operator = input("Enter operator : ")
if operator == "+":
print(first + second)
elif operator == "-":
print(first - second)
elif operator == "*":
print(first * second)
elif operator == "/":
print(first / second)
elif operator == "%":
print(first % second)
else:
print("Invalid Operation")
Range in Python
range() function returns a range object that is a sequence of numbers.
numbers = range(5)
print(numbers)
For iteration (see For Loop section)
While Loop
i = 1
while(i <= 5):
print(i)
i = i + 1
i = 1
while(i <= 5):
print(i * "*")
i = i + 1
i = 5
while(i >= 1):
print(i * "*")
i = i - 1
For Loop (to iterate over a list)
for i in range(5):
print(i)
i = i + 1
for i in range(5):
print(i * "*")
i = i + 1
Lists
List is a complex type in Python.
friends = ["amar", "akbar", "anthony"]
print(friends[0])
print(friends[1])
print(friends[-1])
print(friends[-2])
friends[0] = "aman"
print(friends)
print(friends[0:2]) #returns a new list
for friend in friends:
print(friend)
List Methods :
marks = ["english", 95, "chemistry", 98]
marks.append("physics")
marks.append(97)
print(marks)
marks.insert(0, "math")
marks.insert(1, 99)
print(marks)
print("math" in marks)
print(len(marks)/2)
marks.clear()
print(marks)
i = 0
while i < len(marks):
print(marks[i])
print(marks[i+1])
i = i + 2
Break & Continue
students = ["ram", "shyam", "kishan", "radha", "radhika"]
for student in students:
if(student == "radha"):
break
print(student)
for student in students:
if(student == "kishan"):
continue
print(student)
Tuples
They are like lists (sequence of objects) but they are immutable i.e. once they have been
defined we cannot change them.
Parenthesis in tuples are optional.
marks = (95, 98, 97, 97)
#marks[0] = 98
print(marks.count(97))
print(marks.index(97))
Sets
Sets are a collection of all unique elements.
Indexing is not supported in sets.
marks = {98, 97, 95, 95}
print(marks)
for score in marks:
print(score)
Dictionary
Dictionary is an unordered collection of Items. Dictionary stores a (key, value) pair.
marks = {"math" : 99, "chemistry" : 98, "physics" : 97}
print(marks)
print(marks["chemistry"])
marks["english"] = 95
print(marks)
marks["math"] = 96
print(marks)
Functions in Python
Function is a piece of code that performs some task. (In a tv remote, each button
performs a functions, so a function is like that button in code)
There are 3 types of functions in Java :
a. In-built functions
# int() str() float() min() range() max()
b. Module functions
Module is a file that contains some functions & variables which can be imported
for use in other files.
Each module should contain some related tasks
Example : math, random, string
import math
print(dir(math))
import random
print(dir(random))
import string
print(dir(string))
from math import sqrt
print(sqrt(4))
c. User-defined functions
def sum(a, b=4):
print(a + b)
sum(1, 2)
