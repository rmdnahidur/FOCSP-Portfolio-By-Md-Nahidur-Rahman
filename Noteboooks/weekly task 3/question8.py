number = int(input("Enter a number: "))

if abs(number) > 12:
    print("Error: Number must be between -12 and 12")
else:
    if number >= 0:
        for i in range(13):
            print(f"{i} x {number} = {i * number}")
    else:
        for i in range(12, -1, -1):
            print(f"{i} x {number} = {i * number}")
