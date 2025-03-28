import math

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    # String representation
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    # Addition
    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        raise TypeError("Operand must be of type 'Fraction'")

    # Subtraction
    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    # Multiplication
    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    # Division
    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    # Equality Check
    def __eq__(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator

    # Less than
    def __lt__(self, other):
        return self.numerator * other.denominator < self.denominator * other.numerator

    # Less than or Equal
    def __le__(self, other):
        return self.numerator * other.denominator <= self.denominator * other.numerator

# Testing the Fraction Class
fraction1 = Fraction(3, 4)
fraction2 = Fraction(1, 2)

print("Fraction 1:", fraction1)
print("Fraction 2:", fraction2)

print("\nAddition:", fraction1 + fraction2)
print("Subtraction:", fraction1 - fraction2)
print("Multiplication:", fraction1 * fraction2)
print("Division:", fraction1 / fraction2)

print("\nEquality Check:", fraction1 == fraction2)
print("Fraction1 < Fraction2:", fraction1 < fraction2)
print("Fraction1 <= Fraction2:", fraction1 <= fraction2)
