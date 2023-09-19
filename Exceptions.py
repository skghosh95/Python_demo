Syntax Errors
# A Syntax Error occurs when the parser detects a syntactically incorrect statement.
a = 5 print(a)

Output:
  File "<ipython-input-5-fed4b61d14cd>", line 1
    a = 5 print(a)
              ^
SyntaxError: invalid syntax


Exceptions
# Even if a statement is syntactically correct, it may cause an error when it is executed. This is called an Exception Error.
a = 5 + '10'

Output:

TypeError                                 Traceback (most recent call last)
<ipython-input-6-893398416ed7> in <module>
----> 1 a = 5 + '10'

TypeError: unsupported operand type(s) for +: 'int' and 'str'



Raising an Exception
# If you want to force an exception to occur when a certain condition is met, you can use the raise keyword.

x = -5
if x < 0:
    raise Exception('x should not be negative.')

Output:

Exception                                 Traceback (most recent call last)
<ipython-input-4-2a9e7e673803> in <module>
      1 x = -5
      2 if x < 0:
----> 3     raise Exception('x should not be negative.')

Exception: x should not be negative.


x = -5
assert (x >= 0), 'x is not positive.'
# --> Your code will be fine if x >= 0

Output:
AssertionError                            Traceback (most recent call last)
<ipython-input-7-f9b059c51e45> in <module>
      1 x = -5
----> 2 assert (x >= 0), 'x is not positive.'
      3 # --> Your code will be fine if x >= 0

AssertionError: x is not positive.


Handling Exceptions
# We can use a try and except block to catch and handle exceptions.
# This will catch all possible exceptions
try:
    a = 5 / 0
except:
    print('some error occured.')
    
# You can also catch the type of exception
try:
    a = 5 / 0
except Exception as e:
    print(e)
    
# It is good practice to specify the type of Exception you want to catch.
# Therefore, you have to know the possible errors
try:
    a = 5 / 0
except ZeroDivisionError:
    print('Only a ZeroDivisionError is handled here')
    
# You can run multiple statements in a try block, and catch different possible exceptions
try:
    a = 5 / 1 # Note: No ZeroDivisionError here
    b = a + '10'
except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)
except TypeError as e:
    print('A TypeError occured:', e)

Output:
some error occured.
division by zero
Only a ZeroDivisionError is handled here
A TypeError occured: unsupported operand type(s) for +: 'float' and 'str'













