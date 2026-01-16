import sys

if len(sys.argv) < 2:
    print("Error: No file provided")
    sys.exit()

filename = sys.argv[1]

try:
    with open(filename, 'r') as f:
        for i, line in enumerate(f, start=1):
            print(f"{i}\t{line}", end='')
except FileNotFoundError:
    print("Error: File not found")
