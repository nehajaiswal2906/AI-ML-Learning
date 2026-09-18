# Problem 1 — Prime Factorization

# Given a positive integer n, print its prime factorization.

# Example:

# Input: 360

# Output:

# 2 × 2 × 2 × 3 × 3 × 5
# Constraints
# Don't use a library for factorization.
# Use loops and conditions.
# Don't simply print a hardcoded answer.

n=int(input("Enter the number:"))
prime=[]
for i in range(2,n+1):
    j=2
    flag=True
    while j*j<=i:
        if i%j==0:
            flag=False
            break
        j+=1
    if flag:
        prime.append(i)
lst=[]
for k in prime:
    while n%k==0:
        lst.append(k)
        n=n//k
for i in lst:
    if i==lst[len(lst)-1]:
        print(i,end=" ")
    else:
        print(i,"X",end=" ")


