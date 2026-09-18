# Problem 5 — Alternating Binary Triangle

# For n = 5:

# 1
# 01
# 101
# 0101
# 10101
# Important constraint

# Don't maintain a separate variable that simply alternates between 0 and 1.

# Instead, determine the value from the row and column positions.

# Hint:

# Think about:

# (row + column) % 2

# but work out exactly how you want to use it.

n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print("1",end="")
        else:
            print("0",end="")
    print()
            
