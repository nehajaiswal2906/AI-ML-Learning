
# 🔥 CHALLENGER — Circular Prime

# A number is a Circular Prime if every rotation of its digits is prime.

# For example:

# 197

# Rotations:

# 197
# 971
# 719

# All three are prime.

# Therefore:

# 197 → Circular Prime
# Your task

# Given n, determine whether n is a Circular Prime.

# Think carefully about the steps

# You need to figure out how to:

# Determine the number of digits.
# Generate each rotation.
# Test whether each rotation is prime.
# Stop as soon as one rotation is not prime.

# Don't worry about making it highly optimized yet. Correct logic first.

n=n1=int(input("Enter the number:"))

count=0
while n>0:
    n//=10
    count+=1

n=n1
t=count
for i in range(0,t):
    d=n%10
    n//=10
    n=d*10**(count-1)+n
    flag=False
    divisor=2
    if n==1:
        flag=True
    else:
        while divisor*divisor<=n:
            if n%divisor==0:
                flag=True
                break
            divisor+=1

    if flag:
        break

if flag:
    print("Not a Circular Prime Number.")
else:
    print("Circular Prime.")



