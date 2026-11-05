# Merge two lists into one sorted list, without using .sort()

n=int(input("Enter the number of elements in list 1:"))

numlist1=[]
for i in range (1,n+1):
    numlist1.append(int(input(f"Enter element {i}: ")))

n=int(input("Enter the number of elements in list 1:"))

numlist2=[]
for i in range (1,n+1):
    numlist2.append(int(input(f"Enter element {i}: ")))

numlist=numlist1+numlist2

for i in range (1,len(numlist)):
    for i in range (0,len(numlist)-1):
        if numlist[i]>numlist[i+1]:
            numlist[i+1],numlist[i]=numlist[i],numlist[i+1]

print("The merged sorted list:",numlist)



