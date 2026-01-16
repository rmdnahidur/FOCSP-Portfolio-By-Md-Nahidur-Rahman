# Ask the user for the total number of sweets
sweets = int(input("How many sweets are there? "))

# Ask the user for the total number of pupils
pupils = int(input("How many pupils are present? "))

# Calculate how many sweets each pupil will get using integer division
each = sweets // pupils

# Calculate how many sweets will be left over using modulus
leftover = sweets % pupils

# Display the results
print(f"Each pupil will receive {each} sweets.")
print(f"There will be {leftover} sweets left over.")
