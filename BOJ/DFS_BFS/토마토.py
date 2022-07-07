# 7576
import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

array = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            array.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    q = deque(array)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
                    
bfs()
isValid = True
maximum = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            isValid = False
            break
        maximum = max(graph[i][j], maximum)
    if not isValid:
        break
if isValid:
    if maximum == -1:
        print(-1)
    elif maximum == 1:
        print(0)
    else:
        print(maximum-1)
else:
    print(-1)