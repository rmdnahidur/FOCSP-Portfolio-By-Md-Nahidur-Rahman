import sys

if len(sys.argv) < 3:
    print("Error: Two filenames required")
    sys.exit()

file1, file2 = sys.argv[1], sys.argv[2]

try:
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()

    if content1 == content2:
        print("Files are the same")
    else:
        print("Files are different")
except FileNotFoundError as e:
    print("Error:", e)
