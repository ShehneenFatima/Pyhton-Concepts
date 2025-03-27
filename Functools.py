# Functools
# Module that helps with function manipulation, caching, decorators, and more

# functools.reduce() - Cumulative operations
# Sum of digits
from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 15

# Reduce explanation:
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15

## functools.lru_cache() - Function Caching
# Fibonacci with Caching
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n    
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Output: 55

# functools.partial() - Pre-filling Function Arguments
# partial() helps to create a new function by fixing some arguments of an existing function
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(4))  # Output: 16
print(cube(4))  # Output: 64

# functools.singledispatch() - Function Overloading
# singledispatch() allows a function to behave differently based on the argument type
from functools import singledispatch

@singledispatch
def process(data):
    print(f"Default processing for {data}")

@process.register(str)
def _(data):
    print(f"Processing string: {data.upper()}")

@process.register(int)
def _(data):
    print(f"Processing integer: {data * 2}")

process("hello")  # Output: Processing string: HELLO
process(10)  # Output: Processing integer: 20
process(3.14)  # Output: Default processing for 3.14

# functools.wraps()
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Prevents function name and docstring from being overridden
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    """Says welcome to an intern in the office"""
    print(f"Welcome, {name}")

print(greet.__name__)  # Output: greet
print(greet.__doc__)   # Output: Says welcome to an intern in the office
greet("Ali")  # Calls function and prints decorator output

# *args ,**kwargs
# *args (allows a function to accept any number of positional arguments as a tuple)
# Function with *args
def add_numbers(*args):
    print(args)  # Prints the tuple of arguments
    return sum(args)

print(add_numbers(1, 2, 3, 4, 5))  # Output: (1,2,3,4,5) \n 15

# **kwargs
def user_info(**kwargs):
    print(kwargs)  # Prints dictionary of keyword arguments
    for key, value in kwargs.items():  # Corrected spelling of kwargs
        print(f"{key} : {value}")

user_info(name="Shehneen", age="21", city="Lahore")
# Output:
# {'name': 'Shehneen', 'age': '21', 'city': 'Lahore'}
# name : Shehneen
# age : 21
# city : Lahore
