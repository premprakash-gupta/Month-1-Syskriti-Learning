# Week 2 – Data Types, Variables & Control Flow

## Topics Covered

### 1. Operators
```python
# Arithmetic
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 / 3)   # 3.333...
print(10 // 3)  # 3  (floor division)
print(10 % 3)   # 1  (modulus)
print(10 ** 3)  # 1000 (exponent)

# Comparison
print(5 > 3)    # True
print(5 == 5)   # True
print(5 != 4)   # True

# Logical
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
```

### 2. Conditional Statements
```python
score = 75

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: F")
```

### 3. For Loop
```python
# Loop over a range
for i in range(5):
    print(i)   # 0, 1, 2, 3, 4

# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### 4. While Loop
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### 5. Loop Control Statements
```python
for i in range(10):
    if i == 3:
        continue   # skip 3
    if i == 7:
        break      # stop at 7
    print(i)
```

---

## Key Takeaways
- `if/elif/else` handles branching logic
- `for` loops are best for iterating over sequences
- `while` loops run as long as a condition is `True`
- Use `break` to exit a loop early, `continue` to skip an iteration

---

## Practice Exercises
See the [`exercises/`](./exercises/) folder.
