# 5427
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(int(input())):
    w, h = map(int, input().split())
    graph = [list(input()) for _ in range(h)]
    s_graph, f_graph = [[-1]*w for _ in range(h)], [[-1]*w for _ in range(h)]
    s_q, f_q = deque(), deque()
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '@':
                s_q.append((i, j))
                s_graph[i][j] = 0
            elif graph[i][j] == '*':
                f_q.append((i, j))
                f_graph[i][j] = 0
     
    def bfs():
        while f_q:
            x, y = f_q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if graph[nx][ny] != '#' and f_graph[nx][ny] == -1:
                        f_graph[nx][ny] = f_graph[x][y] + 1
                        f_q.append((nx, ny))
        
        while s_q:
            x, y = s_q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    return s_graph[x][y]
                if graph[nx][ny] == '#' or f_graph[nx][ny] == 0:
                    continue
                if s_graph[x][y] + 1 >= f_graph[nx][ny] or s_graph[nx][ny] != -1:
                    continue
                s_graph[nx][ny] = s_graph[x][y] + 1
                s_q.append((nx, ny))

        return 'IMPOSSIBLE'
    print(bfs())