# prime numbers upto an range
def prime(n):
    list1 = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            list1 += [i]
    print(list1)


prime(50)
