N = int(input())

def dfs(n, cnt, s) -> list:
    if n == 0 and cnt == 0:
        return [s]
    elif n < cnt or cnt < 0:
        return []


    # (
    l = dfs(n-1, cnt + 1, s + '(')
    # )
    r = dfs(n-1, cnt - 1, s + ')')
    return l + r


if N % 2 == 0:
    for p in dfs(N, 0, ''):
        print(p)
