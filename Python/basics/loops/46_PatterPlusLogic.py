# 🧪 Problem 4 — Pattern + Logic

# Given n, print this pattern.

# For n = 5:

# 1
# 22
# 333
# 4444
# 55555

# But there's a catch:

# For rows containing an even number, print the number in reverse order.

# For example, for n = 5:

# 1
# 22
# 333
# 4444
# 55555

# Now modify the problem so that within even-numbered rows the digits alternate:

# 1
# 22
# 333
# 4444
# 55555

# Actually, the output above doesn't show the alternation, so let's make the rule precise:

# For an even row i, print:

# 1010...

# For an odd row i, print:

# 123...

# Therefore for n = 5:

# 1
# 01
# 123
# 0101
# 12345
# Requirements

# Use nested loops and derive the output from the row/column positions.

# No hardcoding.



n=int(input("Enter the number:"))
for i in range(1,n+1):
    if i%2==0:
        for j in range(1,i+1):
            if j%2==0:
                print("1",end="")
            else:
                print("0",end="")
    else:
        for j in range(1,i+1):
            print(j,end="")
    print()
