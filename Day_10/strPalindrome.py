# 3. Check if string is palindrome.
string = input("Enter a string to check:")
newStr = ""
for x in string[::-1]:
    newStr += x.lower()
if newStr == string.lower():
    print("It is palindrome!")
else:
    print("Not a palindrome")
