'''
10.Write a program that takes a distance in kilometers and converts it to miles, 
displaying the result with exactly three decimal places.
'''
# Take distance in kilometers from the user
km = float(input("Enter distance in kilometers: "))

# Conversion factor: 1 km = 0.621371 miles
miles = km * 0.621371

# Display result with 3 decimal places
print("Distance in miles: {:.3f}".format(miles))
