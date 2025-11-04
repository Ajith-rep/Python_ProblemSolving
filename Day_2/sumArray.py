#printing sum all all elements in an array
def Total(arr):
    sum = 0
    for num in arr:
        sum +=num
    return sum

print(Total([1,9,2,8,3,7,4,6,5]))
# #for dynamic input
# arr = list(map(int,input("Enter numbers seperated by space: ").split()))
# print(Total(arr))