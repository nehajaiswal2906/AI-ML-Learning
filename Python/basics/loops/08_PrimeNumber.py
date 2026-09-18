n=int(input("Enter the number:"))
flag=False
if n==1 or n<=0:
    print("Not a Prime number.")
else:
    i=2
    while i*i<=n:
        if n%i==0:
            flag=True
            break
        i+=1
    if flag:
        print("Not a Prime Number.")
    else:
        print("Prime Number.")