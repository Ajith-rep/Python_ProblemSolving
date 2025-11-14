#get each digit from a number in reverse order
num = int(input("Enter a number: "))
while num>0:
    digit = num % 10
    num = num//10
    print(digit, end="")
