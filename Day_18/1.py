# 1.	Create a dictionary where keys are 1,2,3… and values are cubes of keys.
d = {}
for x in range(1, 11):
    d[x] = x**3
print(d)

# 2.	Write a program to sort a dictionary by values
d = {"a": 10, "b": 6, "c": 19, "d": 11, "e": 22}
values = list(d.values())
values.sort()
newd = {}
for x in values:
    for k in d:
        if d[k] == x and k not in newd:
            newd[k] = x
            break

print(newd)

# 3.	Multiply all values in a dictionary.
d = {"a": 10, "b": 6, "c": 19, "d": 11, "e": 22}
res = 1
for x in d.values():
    res *= x
print(res)


# 4.	Write a program to sort a dictionary by keys.

d = {"b": 10, "e": 6, "a": 19, "d": 11, "c": 22}
sorted1 = sorted(d.keys())

newd = {}
for k in sorted1:
    newd[k] = d[k]

# 5.	Keep only those items where values are divisible by 5.
d = {"b": 10, "e": 6, "a": 19, "d": 11, "c": 22, "f": 25}
nd = {}
for x, y in d.items():
    if y % 5 == 0:
        nd[x] = y
print(nd)

# 6.	Find the smallest value in a dictionary.
d = {"b": 10, "e": 6, "a": 19, "d": 11, "c": 22, "f": 25}
small = d["a"]
for x in d.values():
    if x < small:
        small = x
print(min)

# or
vals = list(d.values())
print(min(vals))


# 7.	Find how many values are greater than 10 in a dictionary.
d = {"b": 10, "e": 6, "a": 19, "d": 11, "c": 22, "f": 25}
nd = {}
for v in d:
    if d[v] > 10:
        d[""]
