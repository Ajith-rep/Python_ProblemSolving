#Comparing first and last element in a list
def first_last_same(numberList):
    print("Given List: ",numberList)
    first_num = numberList[0]
    last_num = numberList[-1]

    if(first_num == last_num):
        return True
    else:
        return False

list1 = [10,20,30,40,10]
print("Result is: ",first_last_same(list1))