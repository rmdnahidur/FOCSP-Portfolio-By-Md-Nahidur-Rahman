'''
7.Write a program that takes a list of city names and displays:
The total number of cities entered,
The number of cities that start with the letter 'K',
The list of all cities in alphabetical order
'''
# Get city names from the user (comma separated)
cities = input("Enter city names separated by commas: ").split(',')

# Remove extra spaces from each city name
cities = [city.strip() for city in cities]

# Total number of cities
total_cities = len(cities)

# Count cities starting with 'K' or 'k'
k_cities = 0
for city in cities:
    if city.lower().startswith('k'):
        k_cities += 1

# Sort cities alphabetically
cities.sort()

# Display results
print("Total number of cities:", total_cities)
print("Number of cities starting with 'K':", k_cities)
print("Cities in alphabetical order:", cities)
