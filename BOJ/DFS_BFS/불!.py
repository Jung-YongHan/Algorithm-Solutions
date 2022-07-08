# 4179
# 시작점이 두 종류인 BFS 최단거리 문제
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [list(input()) for _ in range(n)]
f_graph = [[0]*m for _ in range(n)]
j_graph = [[0]*m for _ in range(n)]
f_q = deque()
j_q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'F':
            f_q.append((i, j))
        elif graph[i][j] == 'J':
            j_q.appendleft((i, j))

def bfs():
    while f_q:
        x, y = f_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == '#' or f_graph[nx][ny] != 0:
                continue
            f_graph[nx][ny] = f_graph[x][y] + 1
            f_q.append((nx, ny))

    while j_q:
        x, y = j_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                return j_graph[x][y] + 1
            if graph[nx][ny] == '#' or j_graph[nx][ny] != 0:
                continue
            if f_graph[nx][ny] != 0 and f_graph[nx][ny] <= j_graph[x][y] + 1:
                continue
            j_graph[nx][ny] = j_graph[x][y] + 1
            j_q.append((nx, ny))

    return 'IMPOSSIBLE'
 
print(bfs())