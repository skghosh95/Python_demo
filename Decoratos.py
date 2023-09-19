Decorators
# A decorator is a function that takes another function and extends the behavior of this function without explicitly modifying it. It is a very powerful tool that allows to add new 
# functionality to an existing function.
Function decorators

# A decorator function takes another function as argument, wraps its behaviour inside
# an inner function, and returns the wrapped function.
def start_end_decorator(func):
    
    def wrapper():
        print('Start')
        func()
        print('End')
    return wrapper

def print_name():
    print('Alex')
    
print_name()

print()

# Now wrap the function by passing it as argument to the decorator function
# and asign it to itself -> Our function has extended behaviour!
print_name = start_end_decorator(print_name)
print_name()

Output:
Alex

Start
Alex
End


The decorator syntax
# Instead of wrapping our function and asigning it to itself, we can achieve the same thing simply by decorating our function with an @.

@start_end_decorator
def print_name():
    print('Alex')
    
print_name()

Output:
Start
Alex
End






