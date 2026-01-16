# Import modules for system arguments and statistics
import sys
import statistics

# Get all command-line arguments except the script name
args = sys.argv[1:]

# Check if the user provided any temperature values
if not args:
    print("Error: No temperature values provided")
    sys.exit()  # Exit the program if no values were given

# Create an empty list to store valid temperature numbers
temps = []

# Loop through each argument provided
for arg in args:
    try:
        # Try to convert the argument to a float (number)
        temps.append(float(arg))
    except ValueError:
        # If conversion fails, show which argument is invalid and exit
        print("Invalid temperature:", arg)
        sys.exit()

# Display the highest temperature
print("Maximum:", max(temps))

# Display the lowest temperature
print("Minimum:", min(temps))

# Display the average (mean) temperature
print("Mean:", statistics.mean(temps))
