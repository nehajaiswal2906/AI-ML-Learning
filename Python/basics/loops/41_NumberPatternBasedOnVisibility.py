# Problem 5 — Number Pattern Based on Divisibility

# Given n, print numbers from 1 to n with these rules:

# If divisible by 3, print Three
# If divisible by 5, print Five
# If divisible by both, print ThreeFive
# Otherwise, print the number

# Example for n = 16:

# 1
# 2
# Three
# 4
# Five
# Three
# 7
# 8
# Three
# Five
# 11
# Three
# 13
# 14
# ThreeFive
# 16
# Requirement

# Use a loop and conditional logic.

# Don't use a ready-made FizzBuzz implementation.


n=int(input("Enter the number:"))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print("ThreeFive")
    elif i%3==0:
        print("Three")
    elif i%5==0:
        print("Five")
    else:
        print(i)

