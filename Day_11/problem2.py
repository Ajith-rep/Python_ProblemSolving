# check whether sum of digits except first and last is equal to first and last digit
num = "75547"
first = int(num[0])
last = int(num[-1])
mid_sum = 0

for i in range(1, len(num) - 1):
    mid_sum += int(num[i])

if mid_sum == (first + last):
    print("Equal")
else:
    print("Not Equal")
