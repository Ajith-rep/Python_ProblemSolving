#prg to check whether digits in-between the first and last are less than first and last
num = '8749'
first = int(num[0])
last = int(num[-1])
flag = True
for i in range(1, len(num) - 1):
    mid = int(num[i])
    if not (mid < first and mid < last):
        flag = False
        break
if flag:
    print("True")
else:
    print("False")
