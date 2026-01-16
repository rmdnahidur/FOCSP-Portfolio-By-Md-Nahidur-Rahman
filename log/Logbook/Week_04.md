**Week 4 – Summary Notes**
**Level 4, Semester 1, BSc Computing – Leeds Beckett University**.
**“Functions – Fundamentals of Computer Programming”**.

---

# **Week 4 – Functions in Python**

## **1. Purpose of This Week**

This week introduces **functions**, which are one of the most important parts of programming.
Functions allow programs to be organised, reused, and made easier to understand.

The main topics are:

* Using built-in and imported functions
* Creating your own functions
* Function parameters and return values
* Default and keyword arguments
* Variable length arguments
* Lambda expressions

---

## **2. Using Existing Functions**

Python provides:

* Around **68 built-in functions** (e.g. `print()`, `input()`, `range()`, `type()`)
* Thousands of extra functions in **libraries (modules)**

To use functions from a module, the module must be **imported**.

Example:

```python
import math
print(math.sqrt(25))
```

Here, `math` is the module and `sqrt()` is a function inside it.

You can also import only what you need:

```python
from math import sqrt
print(sqrt(25))
```

This keeps the program clean and avoids confusion.

---

## **3. Importing Data Types**

Some data types are not built-in and must be imported.

Example: `Decimal` type for money calculations.

Normal floating numbers can give small errors:

```python
1.1 + 2.2   # gives 3.3000000000000003
```

Using Decimal:

```python
from decimal import Decimal
print(Decimal("1.1") + Decimal("2.2"))
```

This gives the correct result: `3.3`.

---

## **4. Defining Your Own Functions**

You can create your own functions using the `def` keyword.

Example:

```python
def displayTitle():
    """Displays the title of a movie."""
    print("Life of Brian")
```

The triple-quoted text is a **docstring**.
It explains what the function does and is used to create documentation.

To call the function:

```python
displayTitle()
```

---

## **5. Functions with Parameters**

Functions can receive values (parameters).

Example:

```python
def findMax(a, b):
    """Finds the maximum of two values."""
    if a > b:
        return a
    else:
        return b
```

Calling the function:

```python
findMax(10, 20)
```

* `a` and `b` are **formal parameters**
* `10` and `20` are **arguments**

The `return` statement sends a value back to where the function was called.

---

## **6. Local Variables**

Variables created inside a function:

* Exist only inside that function
* Are destroyed when the function finishes

This helps keep programs safe and organised.

---

## **7. Default Arguments**

Functions can have **default values**.

Example:

```python
def shouldContinue(prompt, answer=False):
```

If `answer` is not provided, it will be `False` automatically.

---

## **8. Keyword Arguments**

You can call a function by naming the parameters.

Example:

```python
showMsg("File opened", prefix="ERROR")
```

Rules:

* Keyword arguments must come after normal arguments
* Each argument can be used only once
* Missing values use defaults

---

## **9. Variable Length Arguments (`*args`)**

Some functions can take many arguments.

Example:

```python
def make_path(*names):
    result = ""
    for name in names:
        result += name + "/"
    return result
```

Calling:

```python
make_path("home", "docs")
make_path("home", "code", "python")
```

The `*` allows any number of arguments.

---

## **10. Arbitrary Keyword Arguments (`**kwargs`)**

Functions can accept unknown keyword arguments.

Example:

```python
def show_details(title="Details", **info):
    print(title)
    for name in info:
        print(name, ":", info[name])
```

Calling:

```python
show_details(title="Error", reason="Disk full")
```

All extra keywords go into a dictionary called `info`.

---

## **11. Lambda Expressions**

A **lambda** is a small anonymous function.

Example:

```python
sqr = lambda num: num * num
sqr(10)
```

Lambda functions:

* Have no name
* Use only one expression
* Are useful inside other functions

Example with `sorted()`:

```python
sorted(students, key=lambda s: s[1])
```

This sorts by the second value in each list.

---

## **12. Week 4 Key Learning Summary**

In Week 4 we learned:

* How to import and use functions from libraries
* How to define our own functions
* How to use parameters and return values
* How default and keyword arguments work
* How to use variable-length arguments
* How lambda expressions create small functions
