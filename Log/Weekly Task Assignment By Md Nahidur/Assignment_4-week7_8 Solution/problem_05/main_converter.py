"""
Main Program
Description:
This program imports the converter module and demonstrates
the conversions: kilometers to miles and Celsius to Fahrenheit.
"""

# Import the converter module
import converter

# Take input from user for kilometers
km = float(input("Enter distance in kilometers: "))
miles = converter.kilometers_to_miles(km)
print(f"{km} km is equal to {miles:.2f} miles.")

# Take input from user for Celsius
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = converter.celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
