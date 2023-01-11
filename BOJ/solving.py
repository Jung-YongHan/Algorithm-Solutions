from collections import deque
import sys

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(u, v):
    q = deque([(u, v)])
    graph[u][v] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = 0

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        u, v = map(int, sys.stdin.readline().split())
        graph[v][u] = 1
    
    result = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                bfs(x, y)
                result += 1

    print(result)