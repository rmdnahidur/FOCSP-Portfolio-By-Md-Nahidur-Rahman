'''
4.Write a function that accepts a list of numbers and returns a new list containing only the even numbers, sorted in ascending order.
'''
def even_numbers_sorted(numbers):
    even_nums = []
    for num in numbers:
        if num % 2 == 0:       # Check if number is even
            even_nums.append(num)
    even_nums.sort()            # Sort in ascending order
    return even_nums

# Example usage
nums = [5, 2, 9, 8, 1, 4]
result = even_numbers_sorted(nums)
print("Even numbers sorted:", result)
