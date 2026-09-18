# 🧪 Problem 5 — Maximum Digit-Sum Difference

# Given n positive integers:

# Find the number with the largest digit sum.
# Find the number with the smallest digit sum.
# Print the difference between those two digit sums.

# Example:

# Input:
# 4
# 123
# 999
# 45
# 1000

# Digit sums:

# 123  → 6
# 999  → 27
# 45   → 9
# 1000 → 1

# Therefore:

# Largest digit sum = 27
# Smallest digit sum = 1

# Difference = 26
# Tie rule

# If multiple numbers have the same digit sum, the number itself doesn't matter for the final difference.


sl=int(input("How many numbers do u want to enter:"))
seq=[]
for i in range (1,sl+1):
    n=int(input("Enter the number:"))
    seq.append(n)
ls=0
ln=0
sn=0
ss=100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
for i in seq:
    s=0
    t=i
    while i>0:
        d=i%10
        i//=10
        s+=d
    if s>=ls:
        ls=s
        ln=t
    if s<=ss:
        ss=s
        sn=t
print("The number with the largest digit sum.",ln)
print("Largest digit sum:",ls)
print("The number with the smallest digit sum.",sn)
print("Smallest digit sum:",ls)


