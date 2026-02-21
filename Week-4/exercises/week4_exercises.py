# Week 4 Exercises – Problem Solving & Basic Algorithms

# Exercise 1: Find Maximum
# Write a function to find the maximum element in a list
# without using the built-in max() function.
def find_max(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

print(find_max([3, 1, 4, 1, 5, 9, 2, 6]))  # 9

# Exercise 2: Linear Search
# Return the index of the target element, or -1 if not found.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search([10, 25, 7, 42, 15], 42))  # 3
print(linear_search([10, 25, 7, 42, 15], 99))  # -1

# Exercise 3: Bubble Sort
# Sort a list in ascending order using bubble sort.
def bubble_sort(arr):
    arr = arr[:]  # work on a copy
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
# [11, 12, 22, 25, 34, 64, 90]

# Exercise 4: Count Occurrences
# Count how many times a target value appears in a list.
def count_occurrences(arr, target):
    count = 0
    for item in arr:
        if item == target:
            count += 1
    return count

print(count_occurrences([1, 2, 3, 2, 4, 2, 5], 2))  # 3

# Exercise 5: Two Sum
# Given a list and a target, find two indices whose values sum to the target.
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
print(two_sum([3, 2, 4], 6))        # [1, 2]
