import sys

A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())
X = int(sys.stdin.readline().strip())

ret = 0
for i in range(A, -1, -1):
    ti = i * 500
    if ti > X:
        continue
    elif ti == X:
        ret += 1
        continue

    for j in range(B, -1, -1):
        tj = ti + j * 100
        if tj > X:
            continue
        elif tj == X:
            ret += 1
            continue

        for k in range(C, -1, -1):
            tk = tj + k * 50
            if tk == X:
                ret += 1
                break
print(ret)
