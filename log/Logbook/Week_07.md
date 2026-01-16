**Week 7 – Summary Notes**
**Level 4, Semester 1 – BSc (hons) Computing (Leeds Beckett University)**.

**“Sets and Dictionaries – Fundamentals of Computer Programming”**.

---

## **1. Purpose of This Week**

This week introduces **Sets** and **Dictionaries**, two important collection types in Python.
They are used to store and manage groups of data in an efficient and organised way.

We learned:

* What sets are and how to use them
* What dictionaries are and how they store data
* How to compare lists, tuples, sets, and dictionaries

---

## **2. Sets in Python**

A **set** is a collection of values where:

* Each value is unique (no duplicates)
* The order does not matter
* Only immutable values can be stored

Example:

```python
vowels = {"a", "e", "i", "o", "u"}
```

Important features:

* Sets do not support indexing
* They support membership testing (`in`)
* They support mathematical operations such as union and intersection

---

## **3. Creating Sets**

A set can be created in different ways:

```python
vowels = {"a", "e", "i", "o", "u"}
empty = set()
vowels = set("aeiou")
```

A **set comprehension** can also be used:

```python
letters = {chr(x) for x in range(97, 123)}
```

---

## **4. Mutable and Immutable Sets**

* A normal **set** can be changed
* A **frozenset** is immutable (cannot be changed)

Example:

```python
suits = frozenset({"heart", "club", "spade", "diamond"})
```

---

## **5. Set Operations**

Sets support useful operations:

| Operation | Meaning                      |                            |
| --------- | ---------------------------- | -------------------------- |
| `         | `                            | Union (combine all values) |
| `&`       | Intersection (common values) |                            |
| `-`       | Difference                   |                            |
| `^`       | Symmetric difference         |                            |

Example:

```python
letters = vowels | consonants
```

Sets can also be compared using `<`, `<=`, `>`, `>=` to test subsets and supersets.

---

## **6. Dictionaries in Python**

A **dictionary** stores data as **key : value** pairs.

Example:

```python
stock = {"apple": 10, "banana": 15, "orange": 11}
```

Important features:

* Keys must be unique
* Values can repeat
* Dictionaries are mutable
* They store data in insertion order

---

## **7. Creating Dictionaries**

Dictionaries can be created in several ways:

```python
grades = {}
stock = dict(apple=10, banana=15)
stock = dict([("apple",10), ("banana",15)])
```

Dictionary comprehensions can also be used:

```python
powers = {x: x**x for x in range(2, 6)}
```

---

## **8. Working with Dictionaries**

Examples:

```python
stock["pear"] = 50
stock["apple"] += 1
del stock["orange"]
```

Checking for a key:

```python
if "apple" in stock:
    print(stock["apple"])
```

---

## **9. Looping Through Dictionaries**

```python
for key in stock:
    print(key)

for value in stock.values():
    print(value)

for key, value in stock.items():
    print(key, value)
```

---

## **10. Dictionaries and Functions**

Dictionaries are used when passing keyword arguments.

Example:

```python
def show(**info):
    print(info)
```

Unpacking a dictionary:

```python
details = {"module":"Databases", "course":"Computing"}
print_module(**details)
```

---

## **11. Choosing the Right Data Type**

| Type       | Best used when             |
| ---------- | -------------------------- |
| List       | Ordered, changeable values |
| Tuple      | Fixed, mixed values        |
| Set        | Unique values, no order    |
| Dictionary | Data linked to keys        |

---

## **12. Week 7 Key Learning Summary**

In Week 7 we learned:

* Sets store unique values
* Sets support union, intersection, and difference
* Dictionaries store data using key–value pairs
* Dictionary comprehensions create dictionaries
* Dictionaries support fast searching using keys
* Choosing the correct data type is important

