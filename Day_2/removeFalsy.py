# Removing falsy values from an array
def removeFalsy(arr):
    falsy = [False, 0, None, ""]
    newArr = []
    for num in arr:
        if num not in falsy:
            newArr += [num]
    # return [x for x in arr if x] (alternate way)
    return newArr


print(removeFalsy([2, 4, False, 12, None]))
