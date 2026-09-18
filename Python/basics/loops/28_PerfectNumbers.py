# Problem 4 — Perfect Numbers

# Print all perfect numbers from 1 to t.

# A perfect number is equal to the sum of its proper divisors.

# For example:

# 6

# Its proper divisors are:

# 1, 2, 3

# and:

# 1 + 2 + 3 = 6

# So 6 is perfect.

# Your program should work for any positive t.

n=int(input("Enter the number:"))
print(f"Perfect Numbers from 1 to {n} are:-")
for k in range (1,n+1):
    s=0
    for t in range (1,k):
        if k%t==0:
            s+=t
    if s==k:
        print(k)