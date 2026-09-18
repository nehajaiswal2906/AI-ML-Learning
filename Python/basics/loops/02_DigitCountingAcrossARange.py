# Problem 2 — Digit Counting Across a Range

# Given n, count how many times the digit 7 appears in all 
# numbers from 1 to n.

# n = 25
# Output = 2

# Don't convert the entire range into strings.

n = int(input("Enter the number:"))
count = 0

for i in range(1, n + 1):
    num = i

    while num > 0:
        d = num % 10
        num = num // 10

        if d == 7:
            count += 1

print(count)