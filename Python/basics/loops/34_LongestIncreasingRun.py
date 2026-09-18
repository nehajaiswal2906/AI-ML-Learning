# Problem 4 — Longest Increasing Run

# Given a sequence of integers, find the length of the longest consecutive strictly increasing run.

# Example:

# Input:
# 1 2 3 2 3 4 5 1

# The longest increasing run is:

# 2 3 4 5

# So:

# Length = 4
# Important

# This is about consecutive elements.

# You're not allowed to skip elements.

sl=int(input("How many numbers do u want to enter in the sequence: ")) 
seq=[]
for i in range(1,sl+1):
    t=int(input(f"Enter number {i}: "))
    seq.append(t)
if sl==1:
    print("Length of longest run: 1")
    print("The longest run is:-",seq[0])
else:
    k=seq[0]
    count=1
    gc=0
    cr=[]
    for i in seq:
        if i>k:
            count+=1
            cr.append(i)
        else:
            count=1
            cr=[i,]
        k=i
        if count>gc:
            gc=count
            lr=cr
    print("Length of longest run:",gc)
    print("The longest run is:-")
    for i in lr:
        print(i,end=" ")