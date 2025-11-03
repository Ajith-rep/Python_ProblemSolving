#print the vowels in a give string in reverse order
strInput = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowelList =""
for ch in strInput:
    if ch in vowels:
        vowelList += ch
print(vowelList[::-1])