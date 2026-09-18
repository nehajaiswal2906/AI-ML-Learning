# 🔥 CHALLENGER — Longest Unique Subarray

# Given a sequence of integers, find the length of the longest contiguous subarray containing 
# no duplicate values.

# Example:

# Input:
# 1 2 3 1 4 5

# One longest valid subarray is:

# 2 3 1 4 5

# So:

# Output: 5

# Another example:

# Input:
# 1 2 1 3 4

# You need to determine the longest contiguous section in which every value is unique.

# Constraints
# Don't use set().
# Don't use external libraries.
# Focus on getting a correct solution first.
# You may use nested loops if that's what you currently know.


sl=int(input("How many numbers do u want to enter in the sequence: ")) 
seq=[]
for i in range(1,sl+1):
    t=int(input(f"Enter number {i}: "))
    seq.append(t)

ns=[]
g=0
for i in seq:
    if i in ns:
        for k in range(0,len(ns)):
            if ns[k]==i:
                break
        ns2=[]
        for t in range (k+1,len(ns)):
            ns2.append(ns[t])
        ns=ns2
        ns.append(i)
    else:
        ns.append(i)
    if len(ns)>g:
        g=len(ns)
print("Length of the longest valid subarray is:",g)

    