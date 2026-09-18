# Problem 1 — Digit Reversal

# Reverse an integer using a while loop.

# Constraints:

# Don't convert it to a string.
# Handle negative numbers.


n=int(input("Enter a number:"))


n1=n # To not lose the original number.
rev=0 # To store the reverse of the number.


while n1>0: # This loop finds the reverse
    l=n1%10
    n1=n1//10
    rev=rev*10+l


print(rev)
