# CHALLENGER — Prime Density

# For every number i from 2 to n, determine whether it is prime.

# Then find the longest consecutive stretch of composite numbers.

# Example:

# n = 20

# You should identify stretches such as:

# 8, 9, 10
# 14, 15, 16

# and return the longest length.


n=int(input("Enter a number:"))
larstreak=0
curstreak=0
num=3
for i in range(2,n+1):
    k=2
    is_prime=True
    while k*k<=i:
        if i%k==0:
            is_prime=False
        k+=1
    if is_prime:
        curstreak=0
    else:
        curstreak+=1
        if curstreak>larstreak:
            larstreak=curstreak
            larstreakseq=i
print("The largest number of streaks are:-",larstreak)
print("The largest streak is:-")
for i in range (larstreak,0,-1):
    larstreakseq=larstreakseq-1
    print(larstreakseq)
