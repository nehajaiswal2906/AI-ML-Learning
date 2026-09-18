# Problem 5 — First Repeating Element

# Given a sequence of integers, find the first element that appears more than once.

# Example:

# Input:
# 4 7 2 7 5 2

# Output:

# 7

# Because 7 is the first value whose occurrence repeats.

# Constraint

# Don't use:

# set()

# or Counter.

# Use loops and your own logic.

sl=int(input("How many numbers do u want to enter in the sequence: ")) 
seq=[]
for i in range(1,sl+1):
    t=int(input(f"Enter number {i}: "))
    seq.append(t)
if sl==1:
    print("There is no element that occurs more than once.")
else:
    ns=[]
    flag=False
    for i in seq:
        if i in ns:
            n=i
            flag=True
            break
        ns.append(i)
    if flag:
        print("The first number that occurs more than once in the sequence is:",n)
    else:
        print("There is no element that occurs more than once.")