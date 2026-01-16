# Ask the user to enter a temperature in Celsius and convert it to a float
celsius = float(input("Enter a temperature in Celsius: "))

# Convert the Celsius temperature to Fahrenheit using the formula
fahrenheit = (celsius * 9/5) + 32

# Display the result in a readable format
print(f"{celsius}C is equivalent to {fahrenheit}F.")
