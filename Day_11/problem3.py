# print middle characters of given string or number:
str1 = input("Enter a string or number: ")
list1 = []
count = 0
for i in str1:
    list1+=i
    count+=1
list2 = ""
for i in range(1,count-1):
    if(list1 is int):
        list2 += int(list1[i])
    else:
        list2 += list1[i]
print(list2, end="")
