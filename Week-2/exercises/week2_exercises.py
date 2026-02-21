# Week 2 Exercises – Data Types, Variables & Control Flow

# Exercise 1: Even or Odd
# Check whether a number is even or odd.
def is_even(n):
    return n % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False

# Exercise 2: FizzBuzz
# Print numbers 1-20. For multiples of 3 print "Fizz",
# for multiples of 5 print "Buzz", for both print "FizzBuzz".
for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Exercise 3: Sum of Natural Numbers
# Calculate the sum of the first n natural numbers using a loop.
def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_natural(10))  # 55

# Exercise 4: Multiplication Table
# Print the multiplication table for a given number.
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

multiplication_table(5)

# Exercise 5: Count Down
# Count down from 10 to 1 using a while loop.
count = 10
while count >= 1:
    print(count)
    count -= 1
print("Blastoff!")
