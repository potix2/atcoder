N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    x, y = list(map(int, input().split()))
    x, y = x - 1, y - 1
    G[x].append(y)
    G[y].append(x)


def dfs(s):
    dist = [-1] * N
    dist[s] = 0

    st = [s]
    while st:
        v = st.pop()
        for nv in G[v]:
            if dist[nv] == -1:
                st.append(nv)
                dist[nv] = dist[v] + 1
    return dist

memo = {}
Q = int(input())
for _ in range(Q):
    a, b = list(map(int, input().split()))
    a, b = a - 1, b - 1
    if not a in memo:
        memo[a] = dfs(a)
    dist = memo[a]
    print(dist[a] + dist[b] + 1)

