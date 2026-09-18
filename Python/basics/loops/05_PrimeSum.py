# Problem 5 — Prime Sum

# Find the sum of all prime numbers between 1 and n.

# Example:

# n = 10


# 2 + 3 + 5 + 7 = 17


n=int(input("Enter the number:"))
sum=0
for i in range (2,n+1):
    k=2
    flag=True
    while k*k<=i:
        if i%k==0:
            flag=False
        k+=1
    if flag:
        sum+=i
print(sum)