# Problem 2 — Right-Aligned Number Triangle

# For n = 5:

#     1
#    12
#   123
#  1234
# 12345

# Your program must work for any positive n.

# Before coding, determine for row i:

# number of spaces = ?
# number of numbers = ?

n=int(input("Enter a number:"))
for i in range (1,n+1):
    for j in range (1,(n-i)+1):
        print(" ",end="")
    for k in range (1,i+1):
        print(k,end="")
    print()