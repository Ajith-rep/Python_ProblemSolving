# Create all pairwise sums of [1,2,3] and [10,20,30] using list comprehension.
l1 = [1, 2, 3]
l2 = [10, 20, 30]
sum = [x + y for x in l1 for y in l2]
print(sum)

# Generate a 3×3 matrix using nested list comprehension.
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)

# Flatten the list [[1,2,3],[4,5],[6]] using list comprehension.
li = [[1, 2, 3], [4, 5], [6]]
new = [y for x in li for y in x]
print(new)

# Generate a list of squares for even numbers and cubes for odd numbers from 1–10.
sc = [x**2 if x % 2 == 0 else x**3 for x in range(1, 10)]
print(sc)

# Extract vowels from the string "Python".
s = "Python"
vowels = [x for x in s if x in "aeiou"]
print(vowels)

# Generate a list of ASCII values for the string "ABC".
a = [ord(x) for x in "ABC"]
print(a)

# Generate uppercase alphabets A–Z using list comprehension.
alpha = [chr(x) for x in range(65, 91)]
print(alpha)

# Capitalize every word in "hello world python".
string = "hello world python"
cap = [x.capitalize() for x in string.split()]
print(cap)

# Print "Even" or "Odd" for numbers 1–10 using list comprehension.
eo = ["even" if x % 2 == 0 else "odd" for x in range(1, 10)]
print(eo)

# Find the length of each word in ["Ajay","Python","Django"].
l1 = ["Ajay", "Python", "Django"]
length = [len(x) for x in l1]
print(length)

# Extract file extensions from ["data.csv","report.pdf","image.png"].
files = ["data.csv", "report.pdf", "image.png"]
ext = [x.split(".")[1] for x in files]
print(ext)

# Create a dictionary where keys are numbers 1–5 and values are their squares.
dict1 = {x: x**2 for x in range(1, 6)}
print(dict1)

# Map characters of "ABC" to their ASCII values using dictionary comprehension.
dicta = {x: ord(x) for x in "ABC"}
print(dicta)

# Combine ['a','b','c'] and [1,2,3] into a dictionary using comprehension.
keys = ["a", "b", "c"]
values = [1, 2, 3]
res = {keys[i]: values[i] for i in range(len(keys))}
print(res)

# Generate all prime numbers between 1 and 100 using list comprehension.
primes = [x for x in range(1, 100) if all(x % y != 0 for y in range(2, x))]
print(primes)

# Create all possible pairs (x, y) from [1,2,3] and [3,1,4] where x ≠ y.
l1 = [1, 2, 3]
l2 = [3, 1, 4]
pairs = [(x, y) for x in l1 for y in l2 if x != y]
print(pairs)

# Generate palindrome numbers between 1 and 100.
palindromes = [x for x in range(1, 100) if str(x) == str(x)[::-1]]
print(palindromes)
# Add elements from two lists [1,2,3] and [10,20,30] using list comprehension.
l1 = [1, 2, 3]
l2 = [10, 20, 30]
l3 = [l1[i] + l2[i] for i in range(len(l1))]
print(l3)

# Extract all student names from [{'name':'Ajay','marks':80},{'name':'Riya','marks':90}].
data = [{"name": "Ajay", "marks": 80}, {"name": "Riya", "marks": 90}]
names = [x["name"] for x in data]
print(names)

# Generate all palindromic numbers between 1 and 1000.
palindromes = [x for x in range(1, 1000) if str(x) == str(x)[::-1]]
print(palindromes)

# Get all words starting with 'a' from ['apple','ant','banana','ball'].
data = ["apple", "ant", "banana", "ball"]
a = [x for x in data if x.startswith("a")]
# or
a = [x for x in data if x[0] == "a"]
print(a)

# Generate numbers between 1 and 20 that are divisible by 2 or 3.
twoand3 = [x for x in range(1, 20) if x % 2 == 0 or x % 3 == 0]
print(twoand3)

# Generate all coordinate pairs [x, y] where x and y range from 0 to 2.
pairs = [[x, y] for x in range(0, 3) for y in range(0, 3)]
print(pairs)
