'''
13.Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2000 (both included). 
'''
# Loop through numbers from 1500 to 2000
for num in range(1500, 2001):  # 2001 because the upper limit is included
    if num % 7 == 0 and num % 5 == 0:
        print(num, end=" ")
