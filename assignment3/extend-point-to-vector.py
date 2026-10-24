
import math


# Task 5.2: Create the Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        return math.sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2
        )


# Task 5.3: Create Vector as a subclass of Point
class Vector(Point):
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)


# Task 5.4: Demonstrate the classes and methods

# Test Point objects
point1 = Point(2, 3)
point2 = Point(2, 3)
point3 = Point(5, 7)

print("Point 1:", point1)
print("Point 2:", point2)
print("Are point1 and point2 equal?", point1 == point2)
print("Are point1 and point3 equal?", point1 == point3)
print("Distance between point1 and point3:", point1.distance(point3))

# Test Vector objects
vector1 = Vector(4, 5)
vector2 = Vector(1, 2)

print("Vector 1:", vector1)
print("Vector 2:", vector2)
print("Vector 1 + Vector 2:", vector1 + vector2)

# Demonstrate that Vector inherits the distance method
print("Distance between vector1 and vector2:", vector1.distance(vector2))
