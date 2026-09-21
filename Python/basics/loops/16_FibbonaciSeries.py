# FIBONACCI SERIES


n=int(input("Enter a number:"))
if n>2:
    a=0
    b=1
    c=0
    k=1
    print("0,1,",end="")
    while k<=n-2:
        c=a+b
        if k!=n-2:
            print(c,end=",")
        else:
            print(c)
        
        a=b
        b=c
        k+=1
elif n==1:
    print("No fibbonaci series for a single Number.")
else:
    print("Invalid input.")
