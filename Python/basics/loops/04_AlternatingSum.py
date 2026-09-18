# Problem 4 — Alternating Sum

# Calculate:

# 1 - 2 + 3 - 4 + 5 - 6 + ... ± n

# Do it using a loop.

# Then modify your program to calculate:

# 1 + 2 - 3 + 4 + 5 - 6 + 7 + 8 - 9 ...

# where every third number is negative.

n=int(input("Enter the number:"))
s=0
for i in range (1,n+1):
    if i%3==0:
        s-=i
    else:
        s+=i
print(s)