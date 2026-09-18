# Problem 4 — Palindromic Number Pyramid

# For n = 5:

#     1
#    121
#   12321
#  1234321
# 123454321

# For n = 4:

#    1
#   121
#  12321
# 1234321
# Requirements
# No hardcoding.
# Arbitrary n.
# Use nested loops.
# The numbers must increase and then decrease.

# Break each row into:

# spaces
# increasing numbers
# decreasing numbers

n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range (n,i,-1):
        print(" ",end="")
    t=1
    for k in range(1,i+1):
        print(t,end="")
        t+=1
    for f in range(i-1,0,-1):
        print(f,end="")
    print()