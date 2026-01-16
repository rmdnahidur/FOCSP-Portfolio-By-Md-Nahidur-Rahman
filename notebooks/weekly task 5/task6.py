# Import modules to work with system arguments and file operations
import sys
import shutil

# Check if the user provided a filename as a command-line argument
if len(sys.argv) < 2:
    print("Error: No filename provided")
    sys.exit()  # Exit the program if no filename is given

# Get the filename from the command-line arguments
filename = sys.argv[1]

# Create a backup filename by adding ".bak" to the original name
backup_name = filename + ".bak"

try:
    # Try to copy the original file to the backup file
    shutil.copy(filename, backup_name)
    print("Backup created:", backup_name)
except FileNotFoundError:
    # If the file does not exist, show an error message
    print("Error: File not found")
