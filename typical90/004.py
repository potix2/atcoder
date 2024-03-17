H, W = list(map(int, input().split()))
A = []
colSum = [0 for _ in range(W)]
rowSum = [0 for _ in range(H)]
for i in range(H):
    row = list(map(int, input().split()))
    for j in range(W):
        colSum[j] += row[j]
        rowSum[i] += row[j]
    A.append(row)

for i in range(H):
    tmp = []
    for j in range(W):
        tmp.append(str(rowSum[i] + colSum[j] - A[i][j]))
    print(" ".join(tmp))
