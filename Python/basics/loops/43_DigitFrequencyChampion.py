# 🧪 Problem 1 — Digit Frequency Champion

# Given n positive integers, find the digit 0–9 that appears the most times across all numbers.

# Example:

# Input:
# 4
# 122
# 345
# 222
# 151

# Count all digits across all four numbers.

# If there is a tie, choose the smaller digit.

# Constraints
# Don't convert numbers to strings.
# Don't use Counter.
# Don't use set().

sl=int(input("Enter the no. of elements in the sequence:"))
ns={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
for i in range(1,sl+1):
    t=int(input(f"Enter Number {i}: "))
    while t>0:
        d=t%10
        t//=10
        ns[d]+=1
g=0
for i in range(0,10):
    if ns[i]>g:
        g=ns[i]
        k=i
print("The digit 0–9 that appears the most times across all numbers:",k)
print("Frequency:",g)

    