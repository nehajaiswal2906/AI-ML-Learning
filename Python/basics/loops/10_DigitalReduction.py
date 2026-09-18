# Problem 2 — Digital Reduction
# Repeatedly sum the digits until one digit remains.
# Example:
# 9875 → 29 → 11 → 2
# Output:
# 2
# Use while.

n=int(input("Enter the number:"))
while n>9:
    s=0
    while n>0:
        l=n%10
        n=n//10
        s=s+l
    n=s
print(n)



