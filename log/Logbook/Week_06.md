**Week 6 – Summary Notes**
**Level 4, Semester 1 – BSc (hons) Computing (Leeds Beckett University)**.

**“Lists and Tuples – Fundamentals of Computer Programming”**.

---

## **1. Purpose of This Week**

This week focuses on **Lists and Tuples**, which are important data types in Python used to store multiple values together.
We learned how to create, modify, and access lists, how to build lists using list comprehensions, and how tuples are used to store fixed groups of data.

---

## **2. Lists in Python**

A **list** is an ordered collection of values.

Example:

```python
squares = [4, 9, 16, 25]
```

Main features of lists:

* They store multiple values in order
* They support indexing, slicing, and looping
* They are **mutable**, meaning values can be changed, added, or removed

---

## **3. List Methods**

Lists have special **methods** that operate on them.

Common list methods include:

* `append()` – adds one item
* `extend()` – adds many items
* `insert()` – adds an item at a specific position
* `remove()` – removes a specific value
* `pop()` – removes and returns an item
* `clear()` – removes all items
* `reverse()` – reverses the list
* `sort()` – sorts the list

Some methods return values:

* `index()` – returns the position of an item
* `count()` – returns how many times an item appears
* `copy()` – creates a new copy of the list

Most list methods change (mutate) the list.

---

## **4. Removing Items Using `del`**

The `del` keyword can remove items from a list.

Examples:

```python
del a[0]       # removes first element
del a[0:5]     # removes first five elements
del a[:]      # clears the list
del a         # deletes the variable
```

---

## **5. List Comprehensions**

A **list comprehension** is a short way to create a list from another sequence.

Example:

```python
squares = [x * x for x in range(10)]
```

With a condition:

```python
even_squares = [x * x for x in range(10) if x % 2 == 0]
```

This creates lists in a clean and efficient way.

---

## **6. Tuples in Python**

A **tuple** is similar to a list, but it is **immutable** (cannot be changed).

Example:

```python
info = ("John", 85, 1.24)
```

Main features:

* Stores multiple values
* Values cannot be changed
* Often contains different types of data

---

## **7. Creating Tuples**

Examples:

```python
empty = ()
single = 4,
info = "Eric", 82, 1.22
```

A tuple can also be created from a list:

```python
t = tuple([1, 2, 3])
```

---

## **8. Accessing Tuple Values**

Tuples can be accessed by:

* **Unpacking**

```python
student = ("Terry", 3.43, "Computing")
name, gpa, course = student
```

* **Indexing**

```python
student[0]
student[1]
```

Tuples cannot be modified after creation.

---

## **9. Tuples and Functions**

Tuples are used to handle variable numbers of arguments.

Example:

```python
def show(*args):
    print(args)
```

A tuple can also be unpacked when calling a function:

```python
data = (2, "Databases", 12)
show(*data)
```

---

## **10. Lists vs Tuples**

| Feature           | List                    | Tuple              |
| ----------------- | ----------------------- | ------------------ |
| Can change values | Yes                     | No                 |
| Data type         | Usually same            | Usually mixed      |
| Use               | Collections that change | Fixed grouped data |

---

## **11. Week 4 Key Learning Summary**

In Week 4 we learned:

* Lists store many values and can be changed
* List methods help to add, remove, and find data
* List comprehensions create lists efficiently
* Tuples store fixed groups of data
* Tuples support unpacking and function arguments
* Lists are mutable, tuples are immutable