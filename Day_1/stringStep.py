word = input("Enter a string: ")
print("Org: ", word)
size = len(word)
for i in range(0, size - 1, 2):
    print(word[i], end=" ")