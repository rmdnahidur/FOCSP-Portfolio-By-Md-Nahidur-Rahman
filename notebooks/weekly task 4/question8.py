# Import the statistics module to calculate the mean
import statistics

# Create an empty list to store the temperatures
temps = []

# Keep asking the user to enter temperatures until they press Enter
while True:
    temp = input("Enter temperature (e.g. 25C) or press Enter to finish: ")

    # If the user presses Enter without typing anything, stop the loop
    if temp == "":
        break

    # Remove the last character ("C") and convert the rest to a number
    value = float(temp[:-1])
    temps.append(value)  # Add the number to our list

# Check if any temperatures were entered
if temps:
    # Display the highest temperature
    print("Maximum:", max(temps), "C")
