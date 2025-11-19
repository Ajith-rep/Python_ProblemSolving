# Reduce Array With Steps Problem
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

target = min(A)
count = 0

for i in range(n):
    diff = A[i] - target

    if B[i] == 0:
        if diff != 0:
            print(-1)
            break
        else:
            continue

    if diff % B[i] != 0:
        print(-1)
        break

    count += diff // B[i]
else:
    print(count)
