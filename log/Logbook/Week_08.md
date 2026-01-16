**Week 8 – Summary Notes**
**Level 4, Semester 1 – BSc (Hons) Computing (Leeds Beckett University)**

**“I/O and File Handling – Fundamentals of Computer Programming”**.

---

## **1. Purpose of This Week**

This week explains how Python programs handle **Input and Output (I/O)** and how they **read and write files**.
These skills are important for building real-world programs that store and process data.

We learned:

* How output can be formatted
* How files are opened, read, and written
* How Python manages file positions and errors

---

## **2. Input and Output (I/O)**

All computer programs follow this process:

**Input → Processing → Output**

So far, we used:

```python
input()
print()
```

However, professional programs also use:

* Files
* Networks
* Other systems for data input and output

---

## **3. Formatting Output**

Python provides several ways to format output so it looks neat and professional.

### **a) F-Strings (Modern Method)**

F-strings allow values to be inserted directly into a string.

Example:

```python
print(f"Your name is {name}")
print(f"The cost is £{price:.2f}")
```

They support:

* Mathematical expressions
* Rounding
* Alignment
* Width control

---

### **b) str.format() Method**

This method replaces placeholders `{}` with values.

Example:

```python
print("Your name is {}".format(name))
print("Cost: £{:.2f}".format(cost))
```

---

### **c) Old %-style Formatting**

This is an older method and is not recommended for new programs.

Example:

```python
print("Price is %.2f" % cost)
```

---

## **4. Files in Python**

Files allow programs to store and retrieve data.

Python treats files as either:

* **Text files**
* **Binary files**

---

## **5. Opening and Closing Files**

Files are opened using `open()`:

```python
f = open("info.txt", "r")
```

After using a file, it must be closed:

```python
f.close()
```

---

## **6. File Modes**

| Mode | Meaning        |
| ---- | -------------- |
| r    | Read           |
| w    | Write          |
| a    | Append         |
| r+   | Read and write |
| b    | Binary mode    |

Example:

```python
f = open("data.txt", "w")
```

---

## **7. Reading from Files**

```python
f.read()       # Reads entire file
f.readline()   # Reads one line
f.readlines()  # Reads all lines as a list
```

Using a loop:

```python
for line in f:
    print(line)
```

---

## **8. Writing to Files**

```python
f.write("Hello")
```

Non-string values must be converted:

```python
f.write(str(50))
```

---

## **9. File Position**

Python keeps track of where it is reading or writing in a file.

```python
f.tell()   # Current position
f.seek(0)  # Move to start of file
```

---

## **10. Using the with Statement**

This is the safest way to work with files:

```python
with open("data.txt") as f:
    lines = f.readlines()
```

The file is automatically closed after use.

---

## **11. Key Learning from Week 7**

In this week, we learned:

* How to format output using f-strings and format()
* How to open, read, and write files
* How file positions work
* Why the `with` statement is important
* How files store program data

---
