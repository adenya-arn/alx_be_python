import math

class Shape:
    """A base class for different shapes."""
    
    def area(self):
        """Method to calculate the area of the shape. To be overridden by derived classes."""
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    """A class to represent a rectangle, inheriting from Shape."""
    
    def __init__(self, length, width):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """A class to represent a circle, inheriting from Shape."""
    
    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)



from polymorphism_demo import Shape, Rectangle, Circle

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()



