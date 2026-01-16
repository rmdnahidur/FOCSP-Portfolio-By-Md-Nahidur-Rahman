# Function to convert Celsius to Fahrenheit
def c_to_f(c):
    # Use the formula F = (C × 9/5) + 32
    return (c * 9 / 5) + 32

# Function to convert Fahrenheit to Celsius
def f_to_c(f):
    # Use the formula C = (F − 32) × 5/9
    return (f - 32) * 5 / 9

# Test the functions with sample values

# Convert 25°C to Fahrenheit
print("25C =", c_to_f(25), "F")

# Convert 77°F to Celsius
print("77F =", f_to_c(77), "C")
