# 🔥 CHALLENGER — Frequency Champion

# Given n positive integers, find the number that has the highest frequency.

# Example:

# Input:
# 8
# 4 7 2 7 4 7 9 4

# Frequencies:

# 4 → 3
# 7 → 3
# 2 → 1
# 9 → 1

# There is a tie between 4 and 7.

# Tie rule

# Choose the smaller number.

# Therefore:

# Output: 4
# Constraints

# Don't use:

# Counter
# set
# sorting

# You'll need to design your own frequency-tracking logic.

sl=int(input("Enter the sequence length:"))
seq=[]
for i in range(1,sl+1):
    t=int(input(f"Enter number {i}: "))
    seq.append(t)

seq2=[]
for i in seq:
    if i not in seq2:
        seq2.append(i)

gc=0
n=0
for i in seq2:
    count=0
    while i in seq:
        count+=1
        seq.remove(i)
    if count>gc:
        gc=count
        n=i
    elif count==gc:
        if i<n:
            n=i

print("The number that has the highest frequency: ",n)
print("Frequency:",gc)

