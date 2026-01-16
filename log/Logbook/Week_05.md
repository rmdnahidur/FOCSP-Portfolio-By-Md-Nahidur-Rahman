**Week 5 – Summary Notes**
**Level 4, Semester 1, BSc (hons) Computing – Leeds Beckett University**.
**“Scripts and Modules – Fundamentals of Computer Programming”**

## **1. Purpose of This Week**

This week explains how Python programs are stored in files and how those files can be used either as **scripts** or as **modules**.
It also explains how Python imports code from other files.

The main topics are:

* Writing and running Python scripts
* Command line arguments
* Creating and importing modules
* Different ways to use `import`
* The module search path
* Using `__name__`

---

## **2. Python Program Files**

When writing real programs, code is saved in **text files** called **scripts**.

* Python program files must:

  * Be plain text
  * Contain valid Python code
  * Have the extension `.py`

Example:

```
average.py
utils.py
```

These files can be executed by Python.

---

## **3. Running a Script**

A script is run from the command line like this:

```
python my_program.py
```

When a script runs:

* The Python interpreter executes every line in the file
* Output only appears when `print()` is used
  (unlike interactive mode)

---

## **4. Command Line Arguments**

Values can be passed to a program when it runs.

Example:

```
python average.py 10.2 8.8 2.6
```

Inside Python, these values are stored in:

```python
sys.argv
```

* `sys.argv[0]` → file name
* `sys.argv[1:]` → values entered by the user

Example:

```python
import sys
values = sys.argv[1:]
```

This allows programs to work with data provided by the user.

---

## **5. What is a Module?**

A **module** is any `.py` file that is imported into another program.

A module:

* Contains functions, variables, or classes
* Can be reused in many programs

Example:

```python
import utils
```

If the file `utils.py` exists, it becomes a module.

---

## **6. Importing Modules**

Modules can be imported in different ways.

### Import whole module

```python
import math
math.sqrt(25)
```

### Import with alias

```python
import math as m
m.sqrt(25)
```

### Import specific items

```python
from math import sqrt, pi
sqrt(25)
```

### Import everything (not recommended)

```python
from math import *
```

This can cause name conflicts.

---

## **7. Module Search Path**

When Python sees an `import` statement, it looks for the module in:

1. Built-in modules
2. Folders listed in `sys.path`
3. The folder where the script is running

Python uses this search path to find the `.py` file.

---

## **8. Using `dir()`**

The `dir()` function shows what is inside a module.

Example:

```python
import math
dir(math)
```

This lists all functions and variables inside the `math` module.

---

## **9. The `__name__` Variable**

Every Python file has a special variable called `__name__`.

* If a file is run as a script:

  ```
  __name__ == "__main__"
  ```
* If the file is imported:

  ```
  __name__ == filename
  ```

This allows one file to act as both:

* A **script**
* A **module**

Example:

```python
if __name__ == "__main__":
    print("This file is running as a script")
```

---

## **10. Why This Is Important**

Using scripts and modules allows:

* Code to be reused
* Programs to be organised
* Large projects to be split into smaller parts

This makes software easier to write, test, and maintain.

---

## **11. Week 4 Key Learning Summary**

In Week 4 we learned:

* Python code is stored in `.py` files
* Files can be run as scripts or imported as modules
* Command line arguments are accessed using `sys.argv`
* Modules are imported using `import`
* Python uses a search path to find modules
* The `__name__` variable helps make flexible programs
