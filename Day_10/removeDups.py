# 2. Remove duplicate characters.
old = "Hello All"
new = ""
for x in old:
    if x not in new:
        new += x
print(new)
