# Zoo Word Validation
word = input().strip()
z = word.count("z")
o = word.count("o")
if o == 2 * z:
    print("Yes")
else:
    print("No")
