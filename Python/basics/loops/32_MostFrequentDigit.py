# Problem 2 — Most Frequent Digit

# Given an integer n, find the digit that occurs the most.

# Example:

# Input: 12233345

# Output:

# 3

# because 3 occurs three times.

# Tie rule

# If two or more digits have the same highest frequency, return the smallest digit.

# Example:

# 112233

# All three occur twice, so output:

# 1

n=int(input("Enter the number:"))
freq={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
while n>0:
    d=n%10
    n//=10
    freq[d]+=1
g=0
gn=0
for i in freq:
    if freq[i]>g:
        g=freq[i]
        gn=i
    elif freq[i]==g:
        if i<gn:
            gn=i
print(gn)


