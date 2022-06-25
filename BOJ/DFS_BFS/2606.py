# 바이러스
from collections import deque
n = int(input())
m = int(input())
info = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    info[u].append(v)
    info[v].append(u)

visited = [False] * (n+1)
def bfs(start, count):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for j in info[v]:
            if not visited[j]:
                queue.append(j)
                visited[j] = True
                count += 1
    return count
count = bfs(1, 0)
print(count)