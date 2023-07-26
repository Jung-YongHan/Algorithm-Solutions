# 14940

from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
start = [(x, y) for x in range(n) for y in range(m) if array[x][y] == 2]

def bfs(x, y):
    q = deque()
    array[x][y] = 0
    visited[x][y] = True
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if array[nx][ny] == 1 and not visited[nx][ny]:
                    array[nx][ny] = array[x][y] + 1
                    visited[nx][ny] = True
                    q.append((nx, ny))

bfs(start[0][0], start[0][1])
for i in range(n):
    for j in range(m):
        if not visited[i][j] and array[i][j] == 1:
            array[i][j] = -1

for i in range(n):
    for j in range(m):
        print(array[i][j], end=' ')
    print()