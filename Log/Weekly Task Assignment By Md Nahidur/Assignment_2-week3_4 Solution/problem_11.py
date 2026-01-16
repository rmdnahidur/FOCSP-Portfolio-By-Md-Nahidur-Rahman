'''
11.Create two sets:
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

Perform the following operations:
(a) Print the union and its size.
(b) Print the difference of setA - setB.
(c) Print the intersection of both sets.
(d) Check whether setA is a subset of setB.
(e) Remove element 7 from setB and display the result.

'''
# Create two sets
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

# (a) Union of both sets and its size
union_set = setA.union(setB)    
print("Union:", union_set)
print("Size of Union:", len(union_set))   

# (b) Difference of setA - setB
difference_set = setA - setB    # Elements only in setA
print("Difference (setA - setB):", difference_set)

# (c) Intersection of both sets
intersection_set = setA.intersection(setB)  
print("Intersection:", intersection_set)

# (d) Check if setA is a subset of setB
is_subset = setA.issubset(setB)  
print("Is setA a subset of setB?", is_subset)

# (e) Remove element 7 from setB
setB.remove(7)      
print("setB after removing 7:", setB)

