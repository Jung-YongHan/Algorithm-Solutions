import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

m, n, h = map(int, input().split())
graph = []
q = deque()
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
        for k in range(m):
            if temp[j][k] == 1:
                q.append((i, j, k))
    graph.append(temp)

while q:
    z, x, y = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                q.append((nz, nx, ny))


def isValid(day):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0:
                    return None
                day = max(graph[i][j][k], day)
    return day

result = isValid(0)
if result is not None:
    print(result-1)
else:
    print(-1)