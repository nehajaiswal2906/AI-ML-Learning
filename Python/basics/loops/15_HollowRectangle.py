# Problem 1 — Hollow Rectangle

# Take rows and columns.

# For:

# rows = 4
# columns = 7

# Output:

# *******
# *     *
# *     *
# *******

# Requirements
# Use nested loops.
# Don't build each row manually.
# Your program must work for arbitrary rows and columns.

# Think: When should you print *, and when should you print a space?

r=int(input("Enter the rows:-"))
c=int(input("Enter the columns:-"))


'''
for i in range (1,r+1):
    if i==1 or i==r:
        print("*"*c,end="")
    else:
        print("*",end="")
        for j in range(1,(c-1)):
            print(" ",end="")
        print("*")
'''

for i in range (1,r+1):
    for j in range (1,c+1):
        if i==1 or i==r or j==1 or j==c:
            print("*",end="")
        else:
            print(" ")
    print()
