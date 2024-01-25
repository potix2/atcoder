import sys

N = int(sys.stdin.readline().rstrip())
A = [int(x) for x in sys.stdin.readline().split()]

ret = 0
done = False
while not done:
    for i in range(N):
        if A[i] % 2 != 0:
            done = True
            break
        A[i] = int(A[i] / 2)
    if not done:
        ret += 1
print(ret)
