# 1260
from collections import deque
import sys

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_d = [False]*(n+1)
visited_b = [False]*(n+1)

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(n+1):
    graph[i].sort()

def dfs(start):
    visited_d[start] = True
    print(start, end=' ')
    for n in graph[start]:
        if not visited_d[n]:
            dfs(n)

def bfs(start):
    q = deque([start])
    visited_b[start] = True
    while q:
        tmp = q.popleft()
        print(tmp, end=' ')
        for n in graph[tmp]:
            if not visited_b[n]: 
                q.append(n)
                visited_b[n] = True

dfs(v)
print()
bfs(v)