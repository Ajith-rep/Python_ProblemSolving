# perfect number
def perfect(n):
    sumDiv = 0
    for i in range(1,n):
        if(n%i == 0):
            sumDiv += i
    if(sumDiv == n):
        print("Perfect Number")
    else:
        print("Not Perfect")

perfect(7)