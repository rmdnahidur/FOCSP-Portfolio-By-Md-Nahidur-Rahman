'''
2.Write a function to check whether a given number is a perfect number or not.
(A perfect number is equal to the sum of its proper divisors, e.g., 6 = 1 + 2 + 3)
'''
def is_perfect(number):
    sum_divisors = 0
    # Find all divisors except the number itself
    for i in range(1, number):
        if number % i == 0:
            sum_divisors += i
    # Check if sum of divisors equals the number
    if sum_divisors == number:
        print(number, "is a perfect number")
    else:
        print(number, "is not a perfect number")

# Get input from user
num = int(input("Enter a number: "))
is_perfect(num)
