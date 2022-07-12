# 2583
import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[False]*m for _ in range(n)]

for i in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for j in range(lx, rx):
        for k in range(ly, ry):
            graph[j][k] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(now_x, now_y):
    q = deque([(now_x, now_y)])
    graph[now_x][now_y] = True
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:
                    graph[nx][ny] = True
                    q.append((nx, ny))
                    count += 1
    return count

result = []
for x in range(n):
    for y in range(m):
        if not graph[x][y]:
            result.append(bfs(x, y))

print(len(result)); print(*sorted(result))