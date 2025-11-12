# 6. Count uppercase and lowercase characters
string = "AjiTh KumAR"
upper = 0
lower = 0
for x in string:
    if x.isupper():
        upper += 1
    else:
        lower += 1
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}")
