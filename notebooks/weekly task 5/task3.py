# Import the sys module to access command-line arguments
import sys

# Get all command-line arguments except the script name
args = sys.argv[1:]

# Check if any arguments were provided
if not args:
    # If no arguments, show an error message
    print("Error: No arguments provided")
else:
    # Sort the arguments by their length (shortest first)
    args.sort(key=len)
    
    # Print the shortest argument
    print("Shortest argument:", args[0])
