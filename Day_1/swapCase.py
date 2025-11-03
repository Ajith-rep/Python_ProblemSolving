# program to swap cases:
strInput = input("Enter a string: ")
# print("Swapcased: ",strInput.swapcase())

# without using swapcase
string = ""
for ch in strInput:
    if ch.isupper():
        string += ch.lower()
    elif ch.islower():
        string += ch.upper()
    else:
        string += ch #for non alpha

print(string)