# Beckett Pizza Plaza – 4-for-3 Special Offer
# Name: Md Nahidur Rahman

# This program calculates the total cost for 4 pizzas,
# applying the "Buy 4, Pay for 3" discount.

import sys

# -------------------------------------------------
# Function to read pizza prices from a text file
# -------------------------------------------------
def read_prices_from_file(filename):
    prices = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()  # remove extra spaces
                if line:  # skip empty lines
                    try:
                        price = float(line)
                        if price <= 0:
                            print(f"Skipping invalid price in file: {price}")
                            continue
                        prices.append(price)
                    except ValueError:
                        print(f"Skipping non-numeric line: {line}")
        return prices
    except FileNotFoundError:
        print(f"File '{filename}' not found. Proceeding to manual input.")
        return []

# -------------------------------------------------
# Function to get pizza prices from the user
# -------------------------------------------------
def get_pizza_prices():
    prices = []
    for i in range(1, 5):
        while True:
            try:
                user_input = input(f"Enter the price of Pizza #{i}: £")
                price = float(user_input)
                if price <= 0:
                    print("Oops! Price must be greater than 0. Try again.")
                    continue
                prices.append(price)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    return prices

# -------------------------------------------------
# Function to calculate total price and discount
# -------------------------------------------------
def calculate_total(prices):
    sorted_prices = sorted(prices)  # sort from lowest to highest
    discount = sorted_prices[0]     # cheapest pizza is free
    total = sum(prices) - discount
    discount_percent = (discount / sum(prices)) * 100
    return total, discount_percent

# -------------------------------------------------
# Main program
# -------------------------------------------------
def main():
    print("Welcome to Beckett Pizza Plaza – 4-for-3 Deal!")
    print("==============================================\n")

    # Use file input if provided as a command-line argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        prices = read_prices_from_file(filename)
        if len(prices) < 4:
            print("Not enough valid prices found in file. Switching to manual entry.\n")
            prices = get_pizza_prices()
        elif len(prices) > 4:
            prices = prices[:4]  # consider only the first 4 pizzas
    else:
        prices = get_pizza_prices()

    # Compute total and discount
    total, discount_percent = calculate_total(prices)

    # Show the results to the user
    print(f"\nYour order total is: £{total:.2f}")
    print(f"You received a generous discount of {discount_percent:.0f}%!")

# -------------------------------------------------
# Run the program
# -------------------------------------------------
if __name__ == "__main__":
    main()
