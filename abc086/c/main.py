import sys


sys.setrecursionlimit(10**9)

N = int(input())

ct = 0
cx = 0
cy = 0

def travel(st, sx, sy, dt, dx, dy):
    check = (dt - st) - (abs(dx - sx) + abs(dy - sy))
    if check >= 0 and (check % 2 == 0):
        return True
    else:
        return False

result = True
for i in range(N):
    t, x, y = list(map(int, input().split()))
    if travel(ct, cx, cy, t, x, y):
        ct = t
        cx = x
        cy = y
    else:
        result = False

if not result:
    print("No")
else:
    print("Yes")
