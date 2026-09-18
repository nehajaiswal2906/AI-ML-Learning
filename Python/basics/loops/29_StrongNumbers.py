# Problem 5 — Strong Numbers

# A number is a Strong Number if the sum of the factorials of its digits equals the number itself.

# Example:

# 145

# because:

# 1! + 4! + 5!
# = 1 + 24 + 120
# = 145

# Find all Strong Numbers from 1 to n.

# Constraint

# Don't use a library function to determine whether a number is strong.

n=int(input("Enter the number:"))

print("The Strong Numbers are:-")
for i in range(1,n+1):
    s=0
    t=i
    while i>0:
        d=i%10
        i//=10
        f=1
        for k in range(1,d+1):
            f*=k
        s+=f
    if s==t:
        print(t)