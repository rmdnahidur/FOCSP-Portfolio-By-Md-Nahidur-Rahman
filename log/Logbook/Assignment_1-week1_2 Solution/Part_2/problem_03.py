'''
3.Write a program to convert Fahrenheit to Celsius and display the result rounded to two decimal places.
'''
# Take Fahrenheit input from the user
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert to Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Round to 2 decimal places
celsius_rounded = round(celsius, 2)

# Display the result
print("Temperature in Celsius:", celsius_rounded)
