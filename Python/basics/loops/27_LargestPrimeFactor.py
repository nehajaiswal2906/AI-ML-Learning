# Problem 2 — Largest Prime Factor

# Given n, find the largest prime factor of n.

# Example:

# Input: 84

# Prime factors:

# 2, 3, 7

# Output:

# 7
# Extra challenge

# Try not to check every number from 2 all the way to n unnecessarily.

t=n=int(input("Enter the number:"))
i=2
n=t
while i*i<=t:
    while n%i==0:
        n//=i
        k=i
    i+=1
if n>1:
    k=n
print("The largest Prime Factor is ",k)
