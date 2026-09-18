# Problem 2 — Longest Arithmetic Run

# Given n integers, find the length of the longest consecutive arithmetic run.

# A sequence is arithmetic if the difference between consecutive elements remains the same.

# Example:

# Input:
# 9
# 2 4 6 8 3 6 9 12 5

# Runs:

# 2 4 6 8       → differences: +2, +2, +2 → length 4

# 3 6 9 12      → differences: +3, +3, +3 → length 4

# So:

# Output:
# 4
# Another example
# 10
# 5 8 11 14 20 18 16 14 10 5

# The run:

# 20 18 16 14

# has:

# -2, -2, -2

# so its length is 4.

# Requirements
# Consecutive elements only.
# The difference must remain constant.
# The difference can be positive, negative, or zero.
# Find the length of the longest run.
# Use loops.
# Don't sort the sequence.
# Edge case

# If there is only one number, the longest arithmetic run has length:

# 1


sl=int(input("Enter the number of elements in the sequence:"))
seq=[]
if sl==1:
    print("The Greatest Arithmetic Run is 1.")
else:
    for i in range(1,sl+1):
        t=int(input(f"Enter number {i}: "))
        seq.append(t)
    k=seq[0]         
    f=seq[1]-seq[0]  
    count=1          
    gc=0             

    for i in seq:
        if i-k==f: 
            count+=1    
        else:
            count=2
        if count>gc:       
            gc=count
        f=i-k
        k=i
    print("The length of the longest consecutive arithmetic run:",gc)
    
