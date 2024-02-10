import sys


sys.setrecursionlimit(10**9)

N = int(input())
memoize = {}
def dp(n):
    if n <= 1:
        return 0

    if memoize.get(n) is not None:
        return memoize[n]

    if n % 2 == 0:
        cost = n + dp(n // 2) * 2
    else:
        cost = n + dp(n // 2) + dp((n // 2) + 1)
    memoize[n] = cost
    return cost

print(dp(N))
