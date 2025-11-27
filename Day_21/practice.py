# Flatten a nested list (one level deep).
l1 = [1, 2, [3, 4], 5, [6, 7]]
flat = []

for x in l1:
    if type(x) is list:
        flat.extend(x)
    else:
        flat.append(x)
print(flat)

# Rotate list to the right by 2.
l1 = [1, 2, 3, 4, 5]
k = 2
rotated = l1[-k: ] + l1[:-k]
print(rotated)

# Rotate list to the left by 3.
l2 = [1,2,3,4,5]
k=3
rotated = l2[k:] + l2[:k]
print(rotated)

# Check if two lists are equal.
l1= [1,4,5,6,9]
l2= [1,4,5,6,9]
isEqual = True
for x in range(len(l1)):
    if l1[x] != l2[x]:
        isEqual = False
        break
if isEqual:
    print("Lists are Equal")
else:
    print("Lists are not equal")



# Find all indices of a given value.
l1 = [1, 3, 7, 3, 2, 3]
val = int(input("Enter a value to search "))

found = False

for x in range(len(l1)):
    if l1[x] == val:
        print(f"At index {x} -> value is {l1[x]}")
        found = True

if not found:
    print("Value Not Found")


# Generate a list of squares up to n.
n = int(input("Enter n: "))
sqr = []
for x in range(1, n + 1):
    sqr.append(x**2)
print(sqr)

# Count positive and negative numbers.
l1 = [4, -3, 7, 0, -1, 9]
nc, pc = 0, 0
for x in l1:
    if x > 0:
        pc += 1
    else:
        nc += 1
print(f"Positive Count: {pc}\nNegative Count: {nc}")