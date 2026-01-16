"""
Program Name: Rectangle Class Example
Description:
This program defines a class 'Rectangle' with attributes length and width.
It has methods to calculate area and perimeter.
Two objects are created and their area and perimeter are displayed.
"""

# Define the Rectangle class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to calculate area
    def area(self):
        return self.length * self.width

    # Method to calculate perimeter
    def perimeter(self):
        return 2 * (self.length + self.width)

# Main program
# Create two Rectangle objects
rect1 = Rectangle(5, 3)
rect2 = Rectangle(10, 7)

# Display results for Rectangle 1
print("Rectangle 1:")
print("Length:", rect1.length, "Width:", rect1.width)
print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())

print("\nRectangle 2:")
# Display results for Rectangle 2
print("Length:", rect2.length, "Width:", rect2.width)
print("Area:", rect2.area())
print("Perimeter:", rect2.perimeter())
