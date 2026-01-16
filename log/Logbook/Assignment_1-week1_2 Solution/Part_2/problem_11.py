'''
11. Write a program to find the Euclidean distance between two coordinates. Take both the coordinates from the user as input.
'''
import math

# Take coordinates from the user
x1 = float(input("Enter x-coordinate of first point: "))
y1 = float(input("Enter y-coordinate of first point: "))
x2 = float(input("Enter x-coordinate of second point: "))
y2 = float(input("Enter y-coordinate of second point: "))

# Calculate Euclidean distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Display the result
print("The Euclidean distance between the points is:", distance)
