# reversed continous number sequence
# i took num variable from 10 because if i take single digit number the spacing is not matching, you can try it taking from 1
num = 10
for i in range(1, 6):
    for j in range(6 - i):
        print(num, end="   ")
        num = num + 1
    print()
