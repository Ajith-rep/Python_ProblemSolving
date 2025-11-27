# Find second largest element.
l1 = [1, 4, 7, 2, 10, 9]
max = l1[0]
second = l1[0]
for x in l1:
    if x > max:
        second = max
        max = x
    elif x > second and x != max:
        second = x
print(second)

# Find third smallest element.
l1 = [1, 23, 63, 34, 85, 60, 70, 18, 39]
first = float("inf")
second = float("inf")
third = float("inf")
for x in l1:
    if x < first:
        third = second
        second = first
        first = x
    elif x < second and x != first:
        third = second
        second = x
    elif x < third and x != first and x != second:
        third = x
print(third)

#Sort list of strings by length.
strl = ["Ajith", "Ravi", "Sandeep", "Ramaswamy"]
strl.sort(key=len)
print(strl)


#Get common elements from two lists.
l1 = [1, 2, 3, 4, 5, 6, 12]
l2 = [2, 4, 6, 8, 10, 12]
l3 = []
for x in l1:
    for y in l2:
        if x == y:
            l3 += [x]
print(l3)


#Get elements only in the first list.
l1 = [1, 2, 3, 4, 5, 6, 12]
l2 = [2, 4, 6, 8, 10, 12]
l3=[]
for x in l1:
    for y in l2:
        if x==y:
            break
    else:
        l3+=[x]
print(l3)

#Merge and remove duplicates from two lists.
# method 1
l1 = [1, 2, 3, 7, 8, 9]
l2 = [1, 2, 3, 23, 45, 88]
l3 = set(l1+l2)
print(l3)

# method 2
l1 = [1, 2, 3, 7, 8, 9]
l2 = [1, 2, 3, 23, 45, 88]
l3 = []
for x in l1 + l2:
    if x not in l3:
        l3 += [x]
print(l3)

#Group list items into sublists of size 2.
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = []
for i in range(0, len(l1),2):
    l2.append([l1[i], l1[i + 1]])
print(l2)

# 16.	Convert list of integers to list of strings.
# method 1
lint = [1,2,3,4,5,6,7,8,9,10]
lintstr= []
for x in lint:
    lintstr += str(x)
print(lintstr)

#method 2
lint = [1,2,3,4,5,6,7,8,9,10]
lintstr= [str(x) for x in lint]
print(lintstr)

# #method 3
lint = [1,2,3,4,5,6,7,8,9,10]
lintstr=list(map(str,lint))
print(lintstr)

# 17.	Convert list of strings to integers.
lintstr = ['1','2','3','4','5','6','7','8','9','10']
lint= []
for x in lintstr:
    lint.append(int(x))
print(lint)

# #method 2
lintstr = ['1','2','3','4','5','6','7','8','9','10']
lint= [int(x) for x in lintstr]
print(lint)

# #method 3
lintstr = ['1','2','3','4','5','6','7','8','9','10']
lint=list(map(int,lintstr))
print(lint)
