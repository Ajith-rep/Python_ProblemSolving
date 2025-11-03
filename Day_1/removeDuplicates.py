# removing duplicate chars in a string
# strInput = input("Enter a string: ")
# chars = ""
# for ch in strInput:
#     if strInput.count(ch) == 1:
#         chars += ch
# print(chars)

# without using count function:
strInput = input("Enter a string: ")
freq = {}

for ch in strInput:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
# print(freq)
result = ""
for ch in strInput:
    if freq[ch] == 1:
        result += ch
print(result)
