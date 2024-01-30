N = int(input())
dict = {}
for i in range(24):
    dict[i] = 0

for i in range(N):
    w, x = map(int, input().split())
    dict[x] = dict[x] + w

m = 0
for i in range(24):
    tmp = 0
    for j in range(9):
        tmp += dict[(i+j) % 24]
    m = max(m, tmp)
print(m)
