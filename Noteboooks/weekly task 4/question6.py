# Ask the user to enter a temperature in Celsius, e.g., "25C"
temp = input("Enter temperature in Centigrade (e.g. 25C): ")

# Remove the last character (the "C") and convert the remaining part to a number
celsius = float(temp[:-1])

# Convert Celsius to Fahrenheit using the formula F = (C × 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Show the result
