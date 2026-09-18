# Problem 1 — Frequency of Digits

# Given a positive integer n, count how many times each digit from 0 to 9 occurs.

# Example:

# Input: 122333

# Output should conceptually be:

# 0 → 0
# 1 → 1
# 2 → 2
# 3 → 3
# 4 → 0
# ...
# Constraints
# Don't use Counter.
# Don't convert the number to a string.
# Use digit extraction.

n=int(input("Enter the number:"))
freq={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
while n>0:
    d=n%10
    n//=10
    freq[d]+=1
for i in freq:
    print(i,"->",freq[i])

    
