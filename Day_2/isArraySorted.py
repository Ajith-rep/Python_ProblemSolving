#checking whether an array is sorted
def isSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
print(isSorted([1,423,6,74]))
print(isSorted([1,4,7,10,234]))