# 5.  Count frequency of characters.
stringA = "aaabbbccddeeeffff"
freq = {}
for char in stringA:
    if char in freq:
        freq[char] = freq[char] + 1
    else:
        freq[char] = 1

for key in freq:
    print(f"{key} occurs {freq[key]} times")
