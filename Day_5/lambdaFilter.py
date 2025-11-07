# filter out even numbers from the list
# nums = [1,2,3,4,5,6]
# even = filter(lambda x: x%2==0, nums)
# print(list(even))

# get only names starting with vowel
# names = ['Ajith','Teja','Om','Isha','Viswa']
# vowels = filter( lambda v: v[0] in 'aeiouAEIOU',names)
# print(list(vowels))

# extract numbers greater than 50
# marks = [45, 67, 89, 23, 50]
# greater50 = filter(lambda x: x > 50, marks)
# print(list(greater50))

#find words longer than 4 characters
# words = ['car','python','ai','machine','data']
# fourChars = filter(lambda char: len(char) > 4,words)
# print(list(fourChars))

#filter palindromic strings:
# words = ['level','apple','madam','python']
# palindrome = filter(lambda str: str[::-1]== str , words)
# print(list(palindrome))