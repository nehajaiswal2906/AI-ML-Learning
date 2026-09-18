# Problem 3 — Hollow Pyramid

# For n = 5:

#     *
#    * *
#   *   *
#  *     *
# *********

# For n = 6:

#      *
#     * *
#    *   *
#   *     *
#  *       *
# ***********
# Requirement

# You need to determine the condition for printing *.

# Don't hardcode the positions.
n=int(input("Enter the number:"))
k=1
for i in range(1,n+1):
    for j in range(n,i,-1): # for gaps
        print(" ",end="")
    print("*",end="")
    if i==1:
        print()
    else:
        if i==n:
            print("*"*k,end="")
        else:
            print(" "*k,end="")
        
        k+=2
        print("*")
