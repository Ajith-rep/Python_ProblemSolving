# Valid Vehicle Tag Problem

s = input().strip()

vowels = "AEIOUY"

if s[2] in vowels:
    print("invalid")
    exit()

pairs = [(0, 1), (3, 4), (4, 5), (7, 8)]

for a, b in pairs:
    if (int(s[a]) + int(s[b])) % 2 != 0:
        print("invalid")
        break
else:
    print("valid")
