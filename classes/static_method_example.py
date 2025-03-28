class Calculator:
    company_name = "Math Utilities Inc."  # Class attribute

    # Instance method: Needs self (specific to an instance)
    def __init__(self, value):
        self.value = value

    def square(self):
        return self.value ** 2

    # Class method: Needs cls (specific to the class)
    @classmethod
    def company_info(cls):
        return f"Company: {cls.company_name}"

    # Static method: Utility function (no access to class or instance)
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

# Testing the Calculator class
calc = Calculator(5)
print("Instance Method - Square of 5:", calc.square())  # Instance method
print(Calculator.company_info())                         # Class method

# Using static methods
print("\nStatic Methods:")
print("Add: 10 + 5 =", Calculator.add(10, 5))
print("Subtract: 10 - 5 =", Calculator.subtract(10, 5))
print("Multiply: 10 * 5 =", Calculator.multiply(10, 5))
print("Divide: 10 / 5 =", Calculator.divide(10, 5))

# Static methods can be called from the instance too
print("\nUsing Static Method from Instance:")
print("Add: 7 + 3 =", calc.add(7, 3))
