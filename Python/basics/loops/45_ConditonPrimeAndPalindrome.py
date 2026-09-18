# Given n, find the first number greater than n that satisfies all three conditions:

# It is prime.
# It is a palindrome.
# Its digit sum is also prime.

# Example structure:

# n = 100

# Your program should search:

# 101 → ?
# 102 → ?
# 103 → ?
# ...

# until it finds the first number satisfying all three conditions.

# Constraint

# You must build the checks yourself using loops.


n=int(input("Enter the number:"))
flag=True
while flag:
    t=n
    s=0
    rev=0
    while n>0: 
        d=n%10
        n//=10
        s+=d
        rev=rev*10+d
    n=t
    palindrome=False
    if rev==t:
        palindrome=True

    i=2
    prime=True
    while i*i<=t:
        if t%i==0:
            prime=False
        i+=1

    i=2
    prime2=True
    while i*i<=s:
        if s%i==0:
            prime2=False
        i+=1
    
    if prime2 and prime and palindrome:
        print("The first number that satisfies all the conditions is ",t)
        flag=False
    n+=1





    

