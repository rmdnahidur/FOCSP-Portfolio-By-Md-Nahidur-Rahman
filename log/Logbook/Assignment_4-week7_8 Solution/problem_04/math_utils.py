
# Function to calculate factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Function to calculate square
def square(n):
    return n * n

# Function to calculate cube
def cube(n):
    return n * n * n
