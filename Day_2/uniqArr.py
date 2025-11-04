#finding unique elements in arr
def uniqueArray(arr):
    newArr = []
    for num in arr:
        if num not in newArr:
            newArr += [num]
    return newArr
#return list(set(arr))  simple and shorter 
print(uniqueArray([1,2,2,3,3,3,4,4,4,4]))