# program to return second largest in an array
# def sLargest(input):
#     sMax = 0
#     for i in input:
#         if i > sMax:
#             sMax = i
#     input = [x for x in input if x!=sMax]
#     sMax = 0
#     for i in input:
#         if i > sMax:
#             sMax = i
#     return sMax

# print(sLargest([34,12,654,73,-2,-35]))


# -------
def sLargest(arr):
    first = second = float("-inf")
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second if second != float("-inf") else None
print(sLargest([23,56,3,-34,129]))
