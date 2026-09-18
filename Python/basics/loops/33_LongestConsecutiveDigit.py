# Problem 3 — Longest Consecutive Digit

# Given an integer, find the longest consecutive run of the same digit.

# Example:

# Input: 111223333221

# Output:

# Digit: 3
# Length: 4

# Because:

# 3333

# is the longest run.

# Think carefully

# You need to keep track of two things:

# current run
# longest run so far


n=int(input("Enter the number:"))
gc=0
k=0
count=1

while n>0:
    d=n%10
    n//=10

    if k==d:
        count+=1
    else:
        count=1

    if count>gc:
        gc=count
        lo=d
    k=d

print("The longest consecutive run ",lo)
print("Number of occurrences",gc)





