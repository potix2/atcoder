import sys

sys.setrecursionlimit(1000000)

H, W = list(map(int, input().split()))
S = []
S.append(['.' for i in range(W+2)])
for i in range(H):
    S.append(list('.' + input() + '.'))
S.append(['.' for i in range(W+2)])

check = [[False for i in range(W+2)] for j in range(H+2)]

def dfs(i,j):
    check[i][j] = True
    for p in [-1,0,1]:
        for q in [-1,0,1]:
            if S[i+p][j+q] == '#' and not check[i+p][j+q]:
                dfs(i+p,j+q)

num = 0
for i in range(1, H + 1, 1):
    for j in range(1, W + 1, 1):
        if S[i][j] == '#' and not check[i][j]:
            dfs(i, j)
            num += 1
print(num)
