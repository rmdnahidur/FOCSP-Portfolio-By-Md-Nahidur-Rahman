'''
10.Create three dictionaries:
a = {

Perform the following tasks:
(a) Merge all dictionaries into a single one.
(b) Add a new pair 'r': 35.
(c) Double all the values in the resulting dictionary.
(d) Delete the key 'y'.
(e) Compute and print the average value of all remaining items.

'''
# Step 1: Create three dictionaries
a = {'x': 5, 'y': 10}
b = {'z': 15, 'w': 20}
c = {'p': 25, 'q': 30}

# (a) Merge all dictionaries
merged = {}
for d in (a, b, c):
    merged.update(d)
print("Merged dictionary:", merged)

# (b) Add a new pair 'r': 35
merged['r'] = 35
print("After adding 'r':", merged)

# (c) Double all the values
for key in merged:
    merged[key] *= 2
print("After doubling values:", merged)

# (d) Delete the key 'y'
if 'y' in merged:
    del merged['y']
print("After deleting 'y':", merged)

# (e) Compute and print the average value
total = sum(merged.values())
count = len(merged)
average = total / count
print("Average value:", average)
