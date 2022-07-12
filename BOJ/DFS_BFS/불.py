# 5427
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(int(input())):
    w, h = map(int, input().split())
    graph = [[0]*w for _ in range(h)]
    s_graph = [[0]*w for _ in range(h)]
    f_graph = [[0]*w for _ in range(h)]
    s_q, f_q = deque(), deque()
    
    for i in range(h):
        temp = input()
        for j in range(w):
            if temp[j] == '#':
                graph[i][j] = -1
            elif temp[j] == '@':
                s_graph[i][j] = 1
                s_q.append((i, j))
            elif temp[j] == '*':
                f_graph[i][j] = 1
                f_q.append((i, j))
            

    def bfs():
        while f_q:
            x, y = f_q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                if graph[nx][ny] == -1:
                    continue
                if f_graph[nx][ny] != 0:
                    continue
                f_graph[nx][ny] = f_graph[x][y] + 1
                f_q.append((nx, ny))

        while s_q:
            x, y = s_q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    return s_graph[x][y]
                if graph[nx][ny] == -1:
                    continue
                if s_graph[nx][ny] != 0:
                    continue
                if f_graph[nx][ny] != 0 and f_graph[nx][ny] <= s_graph[x][y] + 1:
                    continue
                s_graph[nx][ny] = s_graph[x][y] + 1
                s_q.append((nx, ny))

        return 'IMPOSSIBLE'
    
    print(bfs())
    s_graph.clear()
    f_graph.clear()