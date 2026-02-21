# Week 4 – Problem Solving & Basic Algorithms

## Topics Covered

### 1. Introduction to Algorithms
An **algorithm** is a step-by-step procedure to solve a problem.

Good algorithms are:
- **Correct** – produces the right answer
- **Efficient** – uses minimal time and memory
- **Clear** – easy to understand

### 2. Pseudocode Example
```
Algorithm: Find the maximum in a list
Input: A list of numbers
Output: The largest number

SET max = first element of list
FOR each number in the list:
    IF number > max:
        SET max = number
RETURN max
```

Python implementation:
```python
def find_max(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

print(find_max([3, 1, 4, 1, 5, 9, 2, 6]))  # 9
```

### 3. Linear Search
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # return index if found
    return -1          # return -1 if not found

data = [10, 25, 7, 42, 15]
print(linear_search(data, 42))   # 3
print(linear_search(data, 99))   # -1
```
- **Time complexity:** O(n) — checks each element once in the worst case

### 4. Bubble Sort
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

data = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(data))  # [11, 12, 22, 25, 34, 64, 90]
```
- **Time complexity:** O(n²) — not efficient for large datasets

### 5. Big O Notation – Basics

| Complexity | Name | Example |
|------------|------|---------|
| O(1) | Constant | Accessing list element by index |
| O(n) | Linear | Linear search |
| O(n²) | Quadratic | Bubble sort |
| O(log n) | Logarithmic | Binary search |

---

## Key Takeaways
- Break problems into smaller steps before coding
- Linear search works on unsorted data but is slow for large lists
- Bubble sort is simple to understand but inefficient for large inputs
- Big O notation describes how an algorithm's performance scales

---

## Practice Exercises
See the [`exercises/`](./exercises/) folder.
