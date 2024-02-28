N, L = list(map(int, input().split()))
K = int(input())
A = list(map(int, input().split()))


def check(x):
    n = 0
    l = 0
    for i in range(N):
        if A[i] - l >= x:
            n += 1
            l = A[i]


    if L - l >= x:
        n += 1
    return n >= K + 1

left, right = -1, L + 1
while right - left > 1:
    mid = (right + left) // 2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)
