# Problem 4 — Longest Alternating Run

# Given n integers, find the length of the longest 
# consecutive sequence where the numbers alternate
#  between increasing and decreasing.

# For example:

# 1 5 2 7 3 8 4

# The comparisons are:

# 1 < 5 > 2 < 7 > 3 < 8 > 4

# So the entire sequence alternates.

# Output:

# 7

# But:

# 1 5 2 4 3 3 8

# has:

# 1 < 5 > 2 < 4 > 3

# then:

# 3 = 3

# The alternating run breaks there.

# So the longest alternating run before the equality has length 5.

# Rules
# Consecutive elements only.
# > and < must strictly alternate.
# Equal neighboring values break the run.
# Find the length, not necessarily the sequence.
# No sorting.
# Use loops.


sl=int(input("How many numbers do u want to enter in the sequence: ")) 

seq=[]
for i in range(1,sl+1):
    t=int(input(f"Enter number {i}: "))
    seq.append(t)
if sl<2:
    print(sl)
else:
    if seq[0]<=seq[1]:
        g=seq[0]
        count=1
        flag=False
        gc=0
        for i in range(1,len(seq)):
            if flag:
                if seq[i]<g:
                    count+=1  
                    flag=False
                else:
                    count=2
                    flag=True
            else:
                if seq[i]>g:
                    flag=True 
                    count+=1  
                else:
                    count=1
                    flag=False 
            if count>gc:
                gc=count
            g=seq[i] 
        print(gc)
    else:
        g=seq[0]
        count=1
        flag=False
        gc=0
        for i in range(1,len(seq)):
            if flag:
                if seq[i]>g:
                    count+=1  
                    flag=False
                else:
                    count=2
                    flag=True
            else:
                if seq[i]<g:
                    flag=True 
                    count+=1  
                else:
                    count=1
                    flag=False 
            if count>gc:
                gc=count
            g=seq[i] 
        print(gc)