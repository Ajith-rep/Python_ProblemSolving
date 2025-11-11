# Comprehensions are shortcuts for creating new lists, sets, or dictionaries from existing iterables (like lists, strings, or ranges) — all in one line.
# They make your code more compact, readable, and Pythonic.
# syntax: [expression for item in iterable if condition]

# list comprehensions
# nums = [1,2,3,4,5,6,7,8,9,10]
# squares = [num**2 for num in nums]
# print(squares)

# even = [num for num in nums if num % 2==0]
# print(even)


# set comprehensions
# nums = [1, 2, 2, 3, 4]
# unique_squares = {n**2 for n in nums}
# print(unique_squares)


#dict comprehensions
# students = ['Ajith', 'Viswa', 'Swaroop']
# scores = {student: len(student) for student in students}
# print(scores)
