# Problem 1 — Frequency Ranking

# You're given:

# numbers = [
#     4, 7, 2, 4, 9, 7, 4,
#     2, 8, 7, 9, 4, 6, 2
# ]

# Your program must produce the numbers ranked by frequency, from highest frequency to lowest.

# For this input, the expected ranking is conceptually:

# 4 → 4 times
# 2 → 3 times
# 7 → 3 times
# 9 → 2 times
# 6 → 1 time
# 8 → 1 time
# Important requirements
# Do not use collections.Counter.
# Do not use sorted(..., key=...) to magically perform the entire ranking.
# You need to actually reason about the frequencies.



numbers = [4, 7, 2, 4, 9, 7, 4, 2, 8, 7, 9, 4, 6, 2]

numset = set(numbers)

freq = []

for n in numset:
    count = 0

    while n in numbers:
        count += 1
        numbers.remove(n)

    freq.append(count)

pairs = []

for j in range(len(freq)):
    pairs.append([list(numset)[j], freq[j]])

for i in range(len(pairs)):
    for j in range(i + 1, len(pairs)):
        if pairs[j][1] > pairs[i][1] or (
            pairs[j][1] == pairs[i][1] and pairs[j][0] < pairs[i][0]
        ):
            pairs[i], pairs[j] = pairs[j], pairs[i]

for pair in pairs:
    print(f"{pair[0]} → {pair[1]} times")