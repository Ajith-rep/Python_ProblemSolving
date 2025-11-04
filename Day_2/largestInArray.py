# function to return largest element in an array
def largest(input):
    max = 0
    for i in input:
        if i > max:
            max = i
    return max


print(largest([1, 67, 34, 20, -34]))
