# 4179
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
fire_graph = [[0]*m for _ in range(n)]
player_graph = [[0]*m for _ in range(n)]
q1 = deque()
q2 = deque()
for i in range(n):
    temp = list(input())
    for j in range(len(temp)):
        if temp[j] == 'F':
            q1.append((i, j))
        if temp[j] == 'J':
            q2.append((i, j))
    graph.append(temp)

def bfs():
    while q1:
        x, y = q1.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != '#' and fire_graph[nx][ny] == 0:
                    fire_graph[nx][ny] = fire_graph[x][y] + 1
                    q1.append((nx, ny))

    while q2:
        x, y = q2.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != '#' and player_graph[nx][ny] == 0 :
                    if player_graph[nx][ny] + 1 < fire_graph[nx][ny] or fire_graph[nx][ny] != 0:
                        player_graph[nx][ny] = player_graph[x][y] + 1
                        q2.append((nx, ny))
            else:
                return player_graph[x][y] + 1

    return 'IMPOSSIBLE'
 
print(bfs())