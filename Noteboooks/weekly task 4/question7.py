# Import the statistics module to calculate the mean
import statistics

# Create an empty list to store the temperatures
temps = []

# Ask the user to enter 6 temperatures
for i in range(6):
    temp = input("Enter temperature (e.g. 25C): ")  # e.g., "25C"
    value = float(temp[:-1])  # Remove the "C" and convert to a number
    temps.append(value)       # Add the number to the list

# Display the highest temperature
print("Maximum:", max(temps), "C")

# Display the lowest temperature
print("Minimum:", min(temps), "C")

# Display the average (mean) temperature
print("Mean:", statistics.mean(temps), "C")
