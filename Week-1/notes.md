# Week 1 – Introduction to Programming & Python Basics

## Topics Covered

### 1. Setting Up the Environment
- Installed Python 3 and VS Code
- Configured the Python extension
- Ran the first `Hello, World!` program

### 2. How Programs Work
- Source code → interpreter → output
- The Python REPL (Read-Eval-Print Loop)

### 3. Variables and Data Types
```python
name = "Prem"        # str (string)
age = 20             # int (integer)
gpa = 8.5            # float
is_enrolled = True   # bool
```

### 4. Basic Input and Output
```python
# Output
print("Hello, World!")
print(f"My name is {name} and I am {age} years old.")

# Input
user_name = input("Enter your name: ")
print(f"Welcome, {user_name}!")
```

### 5. Type Conversion
```python
num_str = "42"
num_int = int(num_str)      # string → integer
num_float = float(num_str)  # string → float
back_to_str = str(num_int)  # integer → string
```

### 6. Comments
```python
# This is a single-line comment

"""
This is a
multi-line comment / docstring
"""
```

---

## Key Takeaways
- Python uses indentation (4 spaces) to define code blocks
- Variables don't need explicit type declarations
- `print()` and `input()` are the fundamental I/O functions

---

## Practice Exercises
See the [`exercises/`](./exercises/) folder.
