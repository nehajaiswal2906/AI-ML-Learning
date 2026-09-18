# Problem 3 — Divisor Count Champion
# For every number from 1 to n, find its number of divisors.
# Return the number having the most divisors.
# If there's a tie, return the smallest number.

n=int(input("Enter the number:"))
gc=0    # gc denotes greatest count
ngc=0   # ngc denotes number with greatest count
for i in range(1,n+1):

    count=0 
    k=1
    while k*k<=i:
        if i%k==0:
            if k*k==i:
                count+=1
            else:
                count+=2
        k+=1

    if count>gc:
        gc=count
        ngc=i

print(f"The number with most number of divisors upto {n} is",ngc)
        
        
    



