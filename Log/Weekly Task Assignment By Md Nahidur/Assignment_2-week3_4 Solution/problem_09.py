'''
9.Write a function named update_weekly_sales that takes a dictionary of weekly sales data, a day name, and a sale amount.
If the day already exists, update the sale amount by adding the new amount.
If the day does not exist, add it to the dictionary.
Return the updated dictionary.

'x': 5, 'y': 10}
b = {'z': 15, 'w': 20}
c = {'p': 25, 'q': 30}

'''
def update_weekly_sales(sales, day, amount):
    if day in sales:
        sales[day] += amount  # Add to existing amount
    else:
        sales[day] = amount   # Add new day
    return sales

# Example usage
weekly_sales = {'Monday': 200, 'Tuesday': 150}

# Update existing day
weekly_sales = update_weekly_sales(weekly_sales, 'Tuesday', 50)
# Add a new day
weekly_sales = update_weekly_sales(weekly_sales, 'Thursday', 100)

print(weekly_sales)
