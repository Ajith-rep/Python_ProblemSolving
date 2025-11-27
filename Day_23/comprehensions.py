# 1.	Write a list comprehension to generate numbers from 0 to 9.
res = [x for x in range(0, 10)]
print(res)

# 2.	Generate a list of squares of numbers from 1 to 10.
sqr = [x**2 for x in range(1, 11)]
print(sqr)

# 3.	Create a list of even numbers from 1 to 20.
even = [x for x in range(1, 20) if x % 2 == 0]
print(even)


# 4.	Extract each character from the string "python" using list comprehension.
string = "python"
extr = [x for x in string]
print(extr)

# 5.	Convert all characters of "python" to uppercase using list comprehension.
string = "python"
caps = [x.upper() for x in string]
print(caps)

# 6.	Generate all numbers between 1 and 20 that are multiples of 3 or 5.
mults = [x for x in range(1, 20) if x % 3 == 0 or x % 5 == 0]
print(mults)

# 7.	Create a list of squares of odd numbers between 1 and 15.
oddsqrs = [x**2 for x in range(1, 15) if x % 2 != 0]
print(oddsqrs)

# 8.	Generate all numbers between 50 and 100 that end with digit 5.
endswith5 = [x for x in range(50, 100) if x % 10 == 5]
print(endswith5)

# 9.	Reverse each word in the list ["apple", "banana", "cherry"].
strl = ["apple", "banana", "cherry"]
res = [x[::-1] for x in strl]
print(res)

# 10.	Remove all zeros from the list [10, 0, 20, 30, 0, 40].
lis = [10, 0, 20, 30, 0, 40]
res = [x for x in lis if x != 0]
print(res)
