# # 1.	Count + and – numbers
l1 = [1, 9, 5, -2, 3, -6, -22]
pc, nc = 0, 0
for x in l1:
    if x > 0:
        pc += 1
    else:
        nc += 1
print(f"Positive count: {pc}\nNegative Count: {nc}")

# # 2.	Sum of each pair in list of tuple
pairs = [(1, 4), (21, 17), (35, 9), (40, 1), (9, 0)]
res = []
for pair in pairs:
    res.append(sum(pair))
print(res)

# # 3.	Convert 2d to 1d list
l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l2 = []
for x in l1:
    for y in x:
        l2.append(y)
print(l2)

# # 4.	Filter names starting with ‘a’
names = ["ajith", "ravi", "akhil", "mani", "arjun", "srinu"]
a = []
for name in names:
    if name.startswith('a'):
        a.append(name)
print(a)

# # 5.	Get all prime number in list
l1 = [9,4,8,7,13,1,11]
prime = []
for x in l1:
    if x>1:
        for y in range(2,x):
            if x%y == 0:
                break
        else:
            prime.append(x)
print(prime)

# # 6.	Zip two list into a list of tuple
l1 = ["a", "b", "c", 6]
l2 = [1, 2, 3, 4]
res = []
for i in range(len(l1)):
    res.append((l1[i], l2[i]))
print(res)

# 7.	Unzip list of tuple into two lists
t = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
l1 = []
l2 = []
for x in t:
    l1.append(x[0])
    l2.append(x[1])
print(l1)
print(l2)

# # 8.	Move all zeros to end position
l1 = [0, 5, 0, 3, 12, 0, 7]
z=[]
nz=[]
for x in l1:
    if x==0:
        z.append(x)
    else:
        nz.append(x)
print(nz+z)

# 11 Check if a list is sorted or not
k = [10, 11, 12, 12, 12, 15, 18]

is_sorted = True
for x in range(len(k)):
    for y in range(x + 1, len(k)):
        if k[x] > k[y]:
            is_sorted = False
            break
if is_sorted:
    print("List is sorted")
else:
    print("List is not sorted")

# 12
j = [[10, 20, 30], 50, 60, [70, 80, 90]]
k = []
for x in j:
    if type(x) is list:
        k.extend(x)
    else:
        k.append(x)
print(k)

# 13 sum of each col in given matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
temp = []
for x in range(len(matrix)):
    sum1 = 0
    for y in range(len(matrix[x])):
        sum1 += matrix[y][x]
    temp.append(sum1)
print(temp)
