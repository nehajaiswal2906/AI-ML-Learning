# Challenge 3 — Independent coding

# Write a program that takes a list:

# numbers = [12, 5, 8, 12, 20, 5, 7]

# and produces:

# Smallest: 5
# Largest: 20
# 12 appears: 2 times

# Don't use min(), max(), or count() for this one.

n=int(input("Enter the number of elements you want to enter in the list: "))

lst=[]
for i in range (1,n+1):
    lst.append(int(input(f"Enter element {i}: ")))

copylst=lst.copy()
smallest=lst[0]
largest=lst[0]

for i in lst:

    if i<smallest:
        smallest=i

    if i>largest:
        largest=i

print("Smallest Number:",smallest)
print("Largest Number:",largest)

for i in lst: 
    count=0
    while i in copylst:
        count+=1
        copylst.remove(i)
    if count>1:
        print (f"{i} appears: {count} times")
    
