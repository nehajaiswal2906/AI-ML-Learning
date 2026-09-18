# Problem 3 — Remove Repeated Digits

# Given a positive integer, construct a new number by keeping only the first occurrence of each digit.

# Example:

# Input: 12233421

# Result:

# 1234

# The first 1 is kept, first 2 is kept, first 3 is kept, first 4 is kept.

# Constraints
# Don't convert to a string.
# Don't use set().
# Think carefully about the fact that digit extraction happens from right to left.

# That last point is important. You need to decide how you'll preserve the original order.

n=int(input("Enter the number:"))

newnum=0
while n>0:
    d=n%10
    n//=10
    newnum=newnum*10+d

n=newnum
digit=[]
while n>0:
    d=n%10
    n//=10
    if d not in digit:
        digit.append(d)
        
n=0
for i in digit:
    n=n*10+i
print("The new number by keeping only the first occurrence of each digit: ",n)