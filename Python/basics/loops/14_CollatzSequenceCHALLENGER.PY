# 🔥 Challenger — Collatz Sequence

# Given n:

# If n is even → n = n / 2
# If n is odd → n = 3n + 1
# Continue until n = 1

# Return:

# Number of steps
# Maximum value reached

# Example:

# Input: 13

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1


n=int(input("Enter the number:"))


count=0
g=0


while n>1:

    if n>g:
        g=n

    if n%2==0:
        n=n//2
    else:
        n=3*n+1

    count+=1


print(g)
print(count)
    


