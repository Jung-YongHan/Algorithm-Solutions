from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph1, graph2 = [[0]*n for _ in range(n)], [[0]*n for _ in range(n)]
visited1, visited2 = [[False]*n for _ in range(n)], [[False]*n for _ in range(n)]
for i in range(n):
    array = list(input())
    for j in range(n):
        if array[j] == 'G':
            graph1[i][j] = 1
        elif array[j] == 'B':
            graph1[i][j] = 2
            graph2[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs1(x, y):
    q = deque([(x, y)])
    visited1[x][y] = True
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph1[nx][ny] == graph1[x][y] and not visited1[nx][ny]:
                    visited1[nx][ny] = True
                    q.append((nx, ny))

def bfs2(x, y):
    q = deque([(x, y)])
    visited2[x][y] = True
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph2[nx][ny] == graph2[x][y] and not visited2[nx][ny]:
                    visited2[nx][ny] = True
                    q.append((nx, ny))


result1, result2 = 0, 0
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            bfs1(i, j)
            result1 += 1
        if not visited2[i][j]:
            bfs2(i, j)
            result2 += 1
print(result1, result2)
        
