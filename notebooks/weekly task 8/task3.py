import sys

if len(sys.argv) < 3:
    print("Usage: python task3_grep.py <pattern> <filename>")
    sys.exit()

pattern, filename = sys.argv[1], sys.argv[2]

try:
    with open(filename, 'r') as f:
        for line in f:
            if pattern in line:
                print(line, end='')
except FileNotFoundError:
    print("Error: File not found")
