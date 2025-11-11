#Even or Odd Dictionary
nums = [1,2,3,4,5,6,7,8,9,10]

evenOrOdd = {num: ('Even' if num%2 == 0 else 'Odd') for num in nums }
print(evenOrOdd)


#word length mapping
words = ['Ajith','Python','Comprehension']
length = {name:len(name) for name in words}
print(length)

#vowel extraction
sentence = "Decorators and Comprehensions in Python"
vowels = { vowel for vowel in sentence if vowel in 'aeiouAEIOU' }
print(vowels)