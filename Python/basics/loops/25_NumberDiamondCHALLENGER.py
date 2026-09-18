# 🔥 CHALLENGER — Number Diamond

# For n = 4:

#    1
#   121
#  12321
# 1234321
#  12321
#   121
#    1

# For n = 5:

#     1
#    121
#   12321
#  1234321
# 123454321
#  1234321
#   12321
#    121
#     1
# Requirements

# Your program must:

# work for any positive n
# use nested loops
# generate the entire pattern
# contain no hardcoded rows
# 🧠 Before coding

# Don't immediately start typing.

# Figure out the pattern's two halves:

# Upper half
# 1
# 2
# 3
# ...
# n


# Lower half
# n-1
# n-2
# ...
# 1

# Then figure out what changes within each row:

# spaces → ?
# numbers increasing → ?
# numbers decreasing → ?

n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")
    for f in range(i-1,0,-1):
        print(f,end="")
    print()
for i in range(1,n):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(1,(n-i)+1):
        print(k,end="")
    for f in range((n-i)-1,0,-1):
        print(f,end="")
    print()

