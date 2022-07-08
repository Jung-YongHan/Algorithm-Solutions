# 1697
from collections import deque

n, k = map(int, input().split())
graph = [-1] * 100001
graph[n] = 0
move = [-1, 1, 2]
def bfs():
    q = deque([n])
    while q:
        x = q.popleft()
        if x == k:
            return graph[x]
        for nx in [x-1, x+1, 2*x]:
            if 0 <= nx <= 100000 and graph[nx] == -1:
                graph[nx] = graph[x] + 1
                q.append(nx)
print(bfs())