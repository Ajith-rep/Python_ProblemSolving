#Remove all strings from a mixed list.
l1 = ["Ajith",21,"Hello",120,"Tyson",2]
for x in l1:
    if type(x) is str:
        l1.remove(x)
print(l1)

#Find all pairs that add up to a given number.
nums = [1, 3, 4, 5, 6]
target = 7
for x in range(len(nums)):
    for y in range(x+1,len(nums)):
        if(nums[x] + nums[y]) == target:
            print(nums[x],nums[y])

#Calculate running sum list.
n = [1,2,3,4]
new = []
total = 0
for x in n:
    total +=x
    new.append(total)
print(new)

#Reverse a list without using reverse() or slicing.
n1 = [1,2,3,4,5]
new = []
for x in n1:
    new = [x] + new
print(new)


#Find the difference between max and second max.
list1 = [1,54,12,6,99,15]
fmax = 0
smax = 0
for x  in list1:
    if x>fmax:
        smax = fmax
        fmax = x
    elif x>smax and x!=fmax:
        smax = x
diff = fmax - smax
print(f"Difference: {diff}")

# Split a list in half.
li = [1,3,5,7,9,11]
a = []
b = []
length = len(li)
half = length // 2
# Method 1
for x in range(half):
    a.append(li[x])
for y in range(half,length):
    b.append(li[y])
print(f"First Half: {a}\nSecond Half: {b}")

# Method 2
print(f"First Half: {li[:half]}\n Second Half: {li[half:length]}")

# Method 3
for x in range(length):
    if x<half:
        a.append(li[x])
    else:
        b.append(li[x])
print(a,b)

# Group by even and odd.
r = [2,56,23,8,11,92,37,1]
e,o = [],[]
for x in r:
    if x%2==0:
        e+=[x]
    else:
        o +=[x]
print(f"Odd List: {o}\nEven List: {e}")

# Find frequency of each element.
l1 = [1, 2, 1, 3, 2, 1, 4]
freq = {}
for x in l1:
    if x not in freq:
        freq[x] = 1
    else:
        freq[x] += 1
print(freq)

# Find longest string in list.
strings= ["Ajith", "Kumar", "Jack", "Python" , "Bhaskar" ,"California" , "ProblemSolving"]
str1 = {}
for string in strings:
    count = 0
    for s in string:
        count +=1
    str1[string] = count
longest_length = max(str1.values())
for key in str1:
    if str1[key] == longest_length:
        print(key)

# Replace all negative numbers with 0.
n1 = [234,36,1,-352,-4,4,-23]
for x in range(len(n1)):
    if n1[x] < 0:
        n1[x] = 0
print(n1)