# reversing an array
def reverseArr(arr):
    newArr = []
    for i in range(len(arr) - 1, -1, -1):
        newArr += [arr[i]]
    # arr = arr[::-1]
    # return arr
    return newArr


print(reverseArr([1, 2, 3, 4, 5, 6]))
