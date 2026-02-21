# Week 3 – Functions, Lists & Strings

## Topics Covered

### 1. Functions
```python
# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Calling a function
message = greet("Prem")
print(message)   # Hello, Prem!

# Default parameters
def power(base, exp=2):
    return base ** exp

print(power(3))     # 9
print(power(3, 3))  # 27
```

### 2. Lists
```python
numbers = [10, 20, 30, 40, 50]

# Indexing
print(numbers[0])   # 10
print(numbers[-1])  # 50

# Slicing
print(numbers[1:4])   # [20, 30, 40]

# Common methods
numbers.append(60)     # add to end
numbers.insert(0, 5)   # insert at index
numbers.remove(20)     # remove first occurrence
numbers.sort()         # sort in place
print(len(numbers))    # length
```

### 3. List Comprehensions
```python
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)    # [0, 2, 4, 6, 8]
```

### 4. Strings
```python
s = "Hello, World!"

# Common methods
print(s.upper())                          # HELLO, WORLD!
print(s.lower())                          # hello, world!
print(s.replace("World", "Python"))       # Hello, Python!
print(s.split(", "))                      # ['Hello', 'World!']
print(s.strip())                          # removes leading/trailing spaces
print(len(s))                             # 13

# f-strings
name = "Prem"
age = 20
print(f"{name} is {age} years old.")
```

---

## Key Takeaways
- Functions promote code reuse and readability
- Lists are mutable, ordered sequences
- List comprehensions offer a concise way to create lists
- Strings have many built-in methods for text manipulation

---

## Practice Exercises
See the [`exercises/`](./exercises/) folder.
