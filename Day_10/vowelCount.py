# 1. Count number of vowels in a string.
inputStr = "Hello!, How are you?"
voCount = 0
for x in inputStr:
    if x.lower() in "aeiou":
        voCount += 1
print(voCount)
