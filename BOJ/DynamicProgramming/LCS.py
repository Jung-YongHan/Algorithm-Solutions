# 9251
x = input()
y = input()
n, m = len(x), len(y)

if n >= m:
    LCS = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            if x[j] == y[i]:
                LCS[i+1][j+1] = LCS[i][j] + 1
            else:
                LCS[i+1][j+1] = max(LCS[i][j+1], LCS[i+1][j])
else:
    LCS = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if x[i] == y[j]:
                LCS[i + 1][j + 1] = LCS[i][j] + 1
            else:
                LCS[i + 1][j + 1] = max(LCS[i][j + 1], LCS[i + 1][j])
print(LCS[-1][-1])
