N = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

canMake = False
ma = 0
mb = 0
for i in range(N):
    if A[i] != 0 and int(Q[i] / A[i]) > ma:
        ma = int(Q[i] / A[i])
    if B[i] != 0 and int(Q[i] / B[i]) > mb:
        mb = int(Q[i] / B[i])

pos = 0
diff = int((ma + mb)/ 2)
while diff != 0:
    canMake = False
    for i in range(pos + diff):
        check = True
        for j in range(N):
            if Q[j] < A[j] * i + B[j] * (pos - i):
                check = False
                break
        if check:
            canMake = True
            break

    if canMake:
        pos += diff
    else:
        pos -= int(diff / 2)
        diff = int(diff / 2)

print(count)