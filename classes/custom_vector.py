import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Addition of two vectors
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError("Operand must be of type 'Vector'")

    # Subtraction of two vectors
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    # Dot product of two vectors
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    # Magnitude of vector
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # Overriding string representation
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    # Equality comparison
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

# Testing the Vector class
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("Vector 1:", v1)
print("Vector 2:", v2)

# Addition
result_add = v1 + v2
print("\nAddition Result:", result_add)
