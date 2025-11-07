from functools import reduce

nums = [1, 2, 3, 4, 5]
# sum of all numbers in a list
# total = reduce( lambda x,y: x+y, nums)
# print(total)

# maximum number using reduce
# maximum = reduce(lambda m, n: m if m > n else n, nums)
# print(maximum)

# product of all elements in a list
# product = reduce(lambda x, y: x * y, nums)
# print(product)

#concatenate all strings
words = ['Python','is','fun']
# concatenate = reduce ( lambda string1,string2: string1 + string2, words)
# print(concatenate)

#longest word in list
longest = reduce(lambda x , y:x if len(x) > len(y) else y , words)
print(longest)