from datetime import date

class Employee:
    company_name = "Tech Corp"  # Class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Regular instance method
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    # Using @classmethod
    @classmethod
    def company_info(cls):
        return f"Company Name: {cls.company_name}"

    # Factory method using @classmethod
    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = date.today().year
        age = current_year - birth_year
        return cls(name, age)

    # Using @staticmethod
    @staticmethod
    def is_adult(age):
        return age >= 18

# Testing the Employee class
emp1 = Employee("Alice", 28)
emp1.display()

print(Employee.company_info())  # Accessing class-level info

# Creating an instance using @classmethod
emp2 = Employee.from_birth_year("Bob", 1995)
emp2.display()

# Using @staticmethod
print("Is 20 an adult?", Employee.is_adult(20))
print("Is 15 an adult?", Employee.is_adult(15))

