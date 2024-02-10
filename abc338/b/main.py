S = input()
dict = {}
m = 0
result = None
for i in range(len(S)):
    if dict.get(S[i]) is None:
        dict[S[i]] = 1
    else:
        dict[S[i]] += 1

    if dict[S[i]] > m:
        result = S[i]
        m = dict[S[i]]
    elif dict[S[i]] == m and S[i] < result:
        result = S[i]

print(result)