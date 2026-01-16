countries = {}

while True:
    country = input("Enter country name (or press Enter to quit): ").strip()

    if country == "":
        break

    key = country.lower()

    if key in countries:
        print("Capital:", countries[key])
    else:
        capital = input("I don't know the capital. Please enter it: ")
        countries[key] = capital
        print("Capital stored.")
