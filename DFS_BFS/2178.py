# DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m, r = map(int, input().split())
info = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    info[u].append(v)
    info[v].append(u)
for i in range(n+1):
    info[i].sort()

visited_d = [False] * (n+1)
visited_b = [False] * (n+1)
dfs_s = []
bfs_s = []


def dfs(r):
    visited_d[r] = True
    dfs_s.append(r)
    for j in info[r]:
        if not visited_d[j]:
            dfs(j)


def bfs(r):
    queue = deque([r])
    visited_b[r] = True
    bfs_s.append(r)
    while queue:
        v = queue.popleft()
        for j in info[v]:
            if not visited_b[j]:
                queue.append(j)
                visited_b[j] = True
                bfs_s.append(j)

dfs(r)
bfs(r)

print(*dfs_s)
print(*bfs_s)