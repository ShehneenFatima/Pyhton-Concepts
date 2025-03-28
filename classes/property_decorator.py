class Circle:
    def __init__(self, radius):
        self._radius = radius  # Using a private variable

    # Getter method using @property
    @property
    def radius(self):
        return self._radius

    # Setter method using @property
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    # Read-only property
    @property
    def area(self):
        return 3.14159 * (self._radius ** 2)

# Testing the Circle class
circle = Circle(5)
print("Radius:", circle.radius)  # Accessing like an attribute
print("Area:", circle.area)      # Read-only property

circle.radius = 10               # Using the setter
print("Updated Radius:", circle.radius)
print("Updated Area:", circle.area)

# circle.radius = -5  # Uncomment to test the exception

