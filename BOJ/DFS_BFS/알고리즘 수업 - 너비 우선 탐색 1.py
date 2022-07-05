# 알고리즘 수업 - 너비 우선 탐색 1
from collections import deque
import sys
n, m, r = map(int, sys.stdin.readline().split())
info = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    info[u].append(v)
    info[v].append(u)

for i in range(n+1):
    info[i].sort(reverse=True)

visited = [0] * (n + 1)
count = 1


def bfs(r):
    global count
    queue = deque([r])
    visited[r] = count
    while queue:
        v = queue.popleft()
        for j in info[v]:
            if visited[j] == 0:
                count += 1
                queue.append(j)
                visited[j] = count
bfs(r)

for i in visited[1:]:
    print(i)
