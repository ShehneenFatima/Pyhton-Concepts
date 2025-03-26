#1)Generator Functions(use YIELD statement whenever they want to return data)
def countdown(num):
    print("Starting countdown")
    while num > 0:
        yield num
        num -= 1

# Using the generator
for number in countdown(5):
    print(number)
#In this example, the countdown function is a generator that counts down from the provided number to 1. Each call to yield pauses the function and returns the current value of num.


#2) Generator Expressions
# Generator expression
squares = (n * n for n in range(5))

for square in squares:
    print(square)
#Similar to list comprehensions, but with parentheses instead of square brackets. They provide a concise way to create generators.

#Understanding the yield Statement:

#The yield statement is what makes a function a generator. When called, it returns a value and pauses the function's execution, saving its state. Subsequent calls to the generator resume execution right after the yield. This behavior allows generators to produce a sequence of values over time, instead of computing them all at once and sending them back like a list
