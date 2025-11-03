# max , min in a list
list1 = [5, 6, 3, 7, 8, 12, 4]
max = 0
for i in list1:
    if i > max:
        max = i
print(max)
min = list1[0]  # or min = max
for i in list1:
    if min > i:
        min = i
print(min)
