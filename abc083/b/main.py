N, A, B = map(int, input().split())

ret = 0
for i in range(N+1):
    tmp = i
    s = 0
    while tmp > 0:
        s += int(tmp % 10)
        tmp = int(tmp / 10)

    if A <= s <= B:
        ret += i
print(ret)
