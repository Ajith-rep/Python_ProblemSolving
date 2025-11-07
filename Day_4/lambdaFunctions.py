# # Lambda function to concatenate two strings with a space in between
# string1 = "Hello, How are you?"
# string2 = "I am fine, thank you!"
# concat_strings = lambda s1, s2: s1 + " " + s2
# result = concat_strings(string1, string2)
# print(result)
# # Output: Hello, How are you? I am fine, thank you!


# # Lambda function to change the case of a string
# input_string = "Hello World"
# change_case = lambda s: s.upper() if s.islower() else s.lower()
# result_case = change_case(input_string)
# print(result_case)
# # Output: hELLO wORLD

#Lambda function to check if a number is even or odd
# number = 7
# check_even_odd = lambda x : "Even" if x%2==0 else "Odd"
# result_even_odd = check_even_odd(number)
# print(result_even_odd)
# # Output: Odd

# # Lambda function to calculate the square of a number
lambda_square = lambda x: x**2
number_square = 5
result_square = lambda_square(number_square)
print(result_square)
# # Output: 25

