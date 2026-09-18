# Problem 1 — Conditional Sum

# Given n, calculate the sum of all numbers from 1 to n 
# that are:

# divisible by 3
# but NOT divisible by 5

n=int(input("Enter the number:"))
s=0
for i in range(1,n+1):
    if i%3==0 and i%5!=0:
        s+=i
print("Sum:-",s)