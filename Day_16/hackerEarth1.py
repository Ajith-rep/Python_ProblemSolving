# Favourite Singer Problem (Frequency Counting)
from collections import Counter

n = int(input())
arr = list(map(int, input().split()))


freq = Counter(arr)

max_freq = max(freq.values())

print(list(freq.values()).count(max_freq))
