import sys


sys.setrecursionlimit(10**9)

N = int(input())
stage = {}
for i in range(1, N, 1):
    a, b, x = list(map(int, input().split()))
    if (i+1) in stage:
        stage[i+1].append([i, a])
    else:
        stage[i+1] = [[i, a]]

    if x in stage:
        stage[x].append([i, b])
    else:
        stage[x] = [[i, b]]


def dp(n):
    print(n)
    if n == 1:
        return 0

    cost = 1000000000000
    for node in stage[n]:
        print(node)
        cost = min(cost, node[1] + dp(node[0]))
    return cost

print(dp(N))