# program to print vowles in give string and repeated vowel should be printed once
strInput = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowelsList = ""
for ch in strInput:
    if ch in vowels and ch not in vowelsList:
        vowelsList += ch
print(vowelsList)
