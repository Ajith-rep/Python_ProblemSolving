# 4. Replace all vowels with '*'.
sentence = "Hey Everyone, Good Morning!"
newSentence = ""
for char in sentence:
    if char.lower() in "aeiou":
        newSentence += "*"
    else:
        newSentence += char
print(newSentence)
