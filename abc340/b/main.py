Q = int(input())

A = []
for i in range(Q):
    cmd, v = list(map(int, input().split()))
    if cmd == 1:
        A.append(v)
    else:
        print(A[-v])