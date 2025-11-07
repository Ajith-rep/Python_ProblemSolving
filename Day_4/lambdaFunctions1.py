#lambda function with list comprehension
# li = [lambda arg=x: arg*10 for x in range(1,5)]
# for i in li:
#     print(i())

#returning multiple values
# calc = lambda x,y : (x+y , x*y)
# print(calc(7,9))

#lambda function with filter
# n = [1,2,3,4,5]
# even = filter(lambda x: x%2 == 0 , n)
# print(list(even))

#lambda function with map
# n = [1,2,3,4,5,6,7,8,9]
# b = map(lambda x : x*x,n)
# print(list(b))

#lambda function with reduce
# from functools import reduce 
# a = [1,2,3,4,5]
# r = reduce(lambda x,y : x + y , a)
# print(r)

