# Armstrong number is for example:- 
# 153= 1^3+5^3+3^3 
 
n=int(input("Enter the number:")) 
f=n # A new varible so the value of n is not lost. 
nn=n 
# counting the number of digits:- 
count=0 
sum=0 
while n>0: 
    n//=10 
    count+=1 
while nn>0: 
    t=nn%10 
    nn//=10 
    k=count 
    power=1  
    for i in range (1,k+1): 
        power*=t 
    sum+=power 
if sum==f: 
    print("Armstrong Number.") 
else: 
    print("Not an Armstrong number.") 

