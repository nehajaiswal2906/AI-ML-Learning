# Problem 3 — First Special Number

# Starting from n, find the first number greater than n that is both:

# prime
# palindrome

# Use while and stop immediately when you find it. 


n=int(input("Enter a number:"))
n1=n+1
n2=n
n+=1

while True:

    rev=0
    palindrome=False

    while n>0: # Checking Palindrome Number.
        ld=n%10
        n=n//10
        rev=rev*10+ld

    if rev==n1:
        palindrome=True
    
    prime=True
    i=2

    while i*i<=n1: # Checking prime number.
        if n1%i==0:
            prime=False
            break
        i+=1

    if prime and palindrome:
        print(f"Prime and Palindrome Number starting from {n2} is ",n1)
        break
    else:
        n1+=1
        n=n1
    



