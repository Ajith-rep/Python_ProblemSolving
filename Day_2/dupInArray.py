# removing duplicates from an array
def duplicates(arr):
    newArr = []
    for num in arr:
        if num not in newArr:
            newArr += [num]
    return newArr


print(duplicates([34, 52, 60, 12, 34, 1, 24, 1]))
