N = int(input())
a = list(map(int, input().split()))

ret = 0
list.sort(a, reverse=True)
for i in range(N):
    if i % 2 == 0:
        ret += a[i]
    else:
        ret -= a[i]
print(ret)
