# 알고리즘 수업 - 깊이우선탐색 1
import sys
sys.setrecursionlimit(1000000)

n,m,r = map(int, sys.stdin.readline().split())
info = [[] for _ in range(n+1)]
vt = [k for k in range(1, n+1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    info[u].append(v)
    info[v].append(u)
for j in range(n+1):
    info[j].sort()
visited = [0] * (n + 1)
count = 1
visited[r] = count
def dfs(r):
    global count
    for j in info[r]:
        if visited[j] == 0:
            count += 1
            visited[j] = count
            dfs(j)
dfs(r)

for i in visited[1:]:
    print(i)