# Import modules to work with system arguments and web requests
import sys
import urllib.request

# Check if the user provided a URL as a command-line argument
if len(sys.argv) < 2:
    print("Error: No URL provided")
    sys.exit()  # Exit the program if no URL is given

# Get the URL from the command-line arguments
url = sys.argv[1]

try:
    # Try to open the URL
    response = urllib.request.urlopen(url)
    
    # If successful, print a message with the HTTP status code
    print("Website is working. HTTP Status Code:", response.getcode())
except:
    # If any error occurs (e.g., URL is invalid or unreachable), show an error message
    print("Website is not reachable.")
