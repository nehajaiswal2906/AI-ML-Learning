# Problem 5 — GCD

# Find the GCD of two positive integers using a loop.

# Don't use math.gcd().

n1=int(input("Enter Number One:-"))
n2=int(input("Enter Number Two:-"))


if n1>n2: # Finding smallest number between the inputs.
    s=n2
else:
    s=n1


g=0 # Variable to store the greatest divisor

for i in range (1,s+1): # This loop executes till the smalles number.

    if n1%i==0 and n2%i==0:
        if i>g:
            g=i

    
print("The Greatest Common Factor is ",g)
    
