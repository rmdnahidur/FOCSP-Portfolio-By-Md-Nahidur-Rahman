import sys

if len(sys.argv) < 2:
    print("Error: No file provided")
    sys.exit()

filename = sys.argv[1]

try:
    with open(filename, 'r') as f:
        lines = f.readlines()

    line_count = len(lines)
    char_count = sum(len(line) for line in lines)
    word_count = sum(len(line.split()) for line in lines)

    print("Lines:", line_count)
    print("Words:", word_count)
    print("Characters:", char_count)
except FileNotFoundError:
    print("Error: File not found")
