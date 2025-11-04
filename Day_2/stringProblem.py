# Write a program to print all the Upper case letters in the string in reverse  order and then followed by the lower case letters .
str = input("Enter a string: ")
cap = ""
low = ""
for ch in str:
    if ch.isupper():
        cap += ch
    else:
        low += ch
cap = cap[::-1]
print(cap+low)