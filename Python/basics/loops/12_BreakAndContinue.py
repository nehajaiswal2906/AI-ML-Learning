# Problem 4 — break + continue

# Print numbers from 1 to n, but:
# skip multiples of 3
# stop completely when you reach a multiple of 17
# You must use both continue and break.

n=int(input("Enter the number:"))
for i in range (1,n+1):
    if i%3==0:
        continue
    if i%17==0:
        break
    print(i)
