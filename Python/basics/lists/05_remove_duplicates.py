#Remove all duplicates from a list while keeping the original order.

n=int(input("Enter the number of elements:"))
lst=[]

for i in range (1,n+1):
    lst.append(int(input(f"Enter element {i}: ")))
nlst=[]

for i in lst:
    if i not in nlst:
        nlst.append(i)
        
print("The new list without duplicates is:",nlst)