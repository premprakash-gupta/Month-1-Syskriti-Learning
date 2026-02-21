# Week 3 Exercises – Functions, Lists & Strings

# Exercise 1: Factorial
# Write a function that returns the factorial of n.
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))   # 120
print(factorial(0))   # 1

# Exercise 2: Reverse a List
# Write a function that returns a reversed copy of a list.
def reverse_list(lst):
    return lst[::-1]

print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]

# Exercise 3: Count Vowels
# Write a function that counts vowels in a string.
def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

print(count_vowels("Hello, World!"))  # 3

# Exercise 4: Remove Duplicates
# Write a function that removes duplicate values from a list.
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]

# Exercise 5: Palindrome Check
# Write a function that checks whether a string is a palindrome.
def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print(is_palindrome("racecar"))   # True
print(is_palindrome("hello"))     # False
print(is_palindrome("A man a plan a canal Panama".replace(" ", "")))  # True
