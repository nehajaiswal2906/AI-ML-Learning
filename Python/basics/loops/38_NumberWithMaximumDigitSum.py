# Problem 2 — Number With Maximum Digit Sum

# Given n numbers, find the number having the largest digit sum.

# Example:

# Input:
# 5
# 123
# 99
# 45
# 1000
# 78

# Digit sums:

# 123 → 6
# 99  → 18
# 45  → 9
# 1000 → 1
# 78  → 15

# Output:

# 99
# Tie rule

# If two numbers have the same digit sum, choose the smaller number.

sl=int(input("How many numbers do u want to enter : ")) 
g=0
for i in range(1,sl+1):
    t=int(input(f"Enter number {i}: "))
    n=t
    s=0
    while t>0:
        d=t%10
        t//=10
        s+=d
    if s>g:
        g=s
        num=n
    elif s==g:
        if num>n:
            num=n
print("The number with Largest digit sum is:",num)
print("Sum",g)
