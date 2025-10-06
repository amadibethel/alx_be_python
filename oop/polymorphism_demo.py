# File: oop/polymorphism_demo.py

import math


class Shape:
    """Base class representing a generic geometric shape."""

    def area(self):
        """Placeholder method to be overridden by derived classes."""
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    """Derived class representing a rectangle."""

    def __init__(self, length, width):
        """Initialize the length and width of the rectangle."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""

    def __init__(self, radius):
        """Initialize the radius of the circle."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)
