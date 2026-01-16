def factors(number):
    result = []

    for i in range(1, number + 1):
        if number % i == 0:
            result.append(i)

    return result


# Test program
num = int(input("Enter an integer: "))
print("Factors:", factors(num))
