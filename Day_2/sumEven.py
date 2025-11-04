# printing sum of even numbers in an array
def evenSum(arr):
    sum = 0
    for num in arr:
        if num % 2 == 0:
            sum += num
        else:
            continue
    return sum


print(evenSum([1, 2, 3, 4, 6, 7, 9]))
print(evenSum([1, 3, 5, 7, 9]))
