'''
7.Write a program that takes a temperature in Celsius and prints whether it’s Cold (<10°C), Warm (10–25°C), or Hot (>25°C).
'''
# Take temperature input from the user
temp = float(input("Enter temperature in Celsius: "))

# Check the temperature category
if temp < 10:
    print("It's Cold.")
elif 10 <= temp <= 25:
    print("It's Warm.")
else:
    print("It's Hot.")
