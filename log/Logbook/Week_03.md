# Week 3 – Control Statements & Program Logic
# Level 4 – Semester 1 – BSc (Hons) Computing – Leeds Beckett University

# -----------------------------
# 1. Purpose of This Week
# -----------------------------
# Learn how programs make decisions and repeat actions using control statements
# Topics: Boolean expressions, if/elif/else, logical operators, loops, break/continue, ternary operator

# -----------------------------
# 2. Algorithms & Control Flow
# -----------------------------
# Algorithms are sets of steps to solve problems
# Structures:
# - Sequence: steps run one after another
# - Selection: choose which steps to run
# - Iteration: repeat steps
# Selection and iteration use Boolean expressions

# -----------------------------
# 3. Boolean Expressions
# -----------------------------
# Return True or False
# Relational operators: > < >= <= == !=

age = 20
print(age > 18)  # True

# -----------------------------
# 4. if Statement
# -----------------------------
number1 = 10
number2 = 5

if number1 > number2:
    print("number1 is greater")

# -----------------------------
# 5. if...else and elif
# -----------------------------
if number1 > number2:
    print("number1 is greater")
else:
    print("number2 is greater or equal")

if number1 > number2:
    print("greater")
elif number1 == number2:
    print("equal")
else:
    print("smaller")

# -----------------------------
# 6. Logical Operators
# -----------------------------
# and, or, not
male = True

if age >= 18 and age <= 65:
    print("Working age")

if (age >= 18 and age <= 65) or male:
    print("Condition met")

# -----------------------------
# 7. Membership Testing
# -----------------------------
names = ["Eric", "Terry", "John"]

if "Eric" in names:
    print("Eric is in the list")

word = "hello"
sentence = "hi world"
if word not in sentence:
    print("Word not found")

# -----------------------------
# 8. Ternary Operator
# -----------------------------
a, b = 5, 10
highest = a if a > b else b
print(highest)

# -----------------------------
# 9. while Loop
# -----------------------------
x = 5
while x > 0:
    print(x)
    x -= 1

# -----------------------------
# 10. for Loop
# -----------------------------
for n in names:
    print(n)

# -----------------------------
# 11. range() Function
# -----------------------------
for i in range(10):  # 0 to 9
    print(i)

for i in range(10, 20, 2):  # 10,12,14,16,18
    print(i)

# -----------------------------
# 12. break and continue
# -----------------------------
for n in names:
    if n == "John":
        break   # stops the loop

for n in names:
    if "a" in n:
        continue  # skips this iteration
    print(n)

# -----------------------------
# 13. Nested Loops
# -----------------------------
for i in range(1, 5):
    for j in range(1, 5):
        print(i, j)  # i loop inside j loop

# -----------------------------
# 14. Week 3 Summary
# -----------------------------
# - Selection and iteration control program flow
# - Boolean expressions decide conditions
# - if, elif, else make decisions
# - while and for create loops
# - break and continue modify loop behavior
# - Ternary operators return values based on conditions
# - Nested loops are possible but can be complex
