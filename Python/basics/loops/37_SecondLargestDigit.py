# Problem 1 — Second Largest Digit

# Given a positive integer n, find the second largest distinct digit in it.

# Example:

# Input: 583527

# Distinct digits:

# 8, 5, 3, 2, 7

# Output:

# 7

# because 8 is largest and 7 is second largest.

# Requirements
# Don't convert the number to a string.
# Don't sort anything.
# Don't use set().
# Edge case

# If there is no second distinct digit, print an appropriate message.

n=int(input("Enter the number:"))
sl=-1
l=-1
flag=False
while n>0: 
    d=n%10
    n//=10 
    if d>=l: 
        if d!=l:
            sl=l
        l=d   
    elif d>sl:
        sl=d
if sl!=-1:
    print("The second largest digit is ",sl)
else:
    print("There is no second distinct digit.")