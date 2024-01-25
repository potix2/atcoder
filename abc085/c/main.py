N, Y = map(int, input().split())

def ans():
    for i in range(int(Y/10000), -1, -1):
        t1 = Y - i * 10000
        for j in range(int(t1/5000), -1, -1):
            t2 = t1 - j * 5000
            k = int(t2 / 1000)
            if k + i + j == N:
                return [i, j, k]
    return [-1, -1, -1]

print(*ans())
