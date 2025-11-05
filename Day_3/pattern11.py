#diamond
# pyramid
for i in range(5):
    for j in range(5 - i):
        print(" ", end=" ")
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()
# reverse pyramid
for i in range(4,0,-1):
    for j in range(6 - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()
