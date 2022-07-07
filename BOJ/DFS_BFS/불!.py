# # 4179
# import sys
# from collections import deque
# import copy
# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(input()))

# player = []
# fire = []
# player_graph = copy.deepcopy(graph)
# fire_graph = copy.deepcopy(graph)
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 'J':
#             player.append((i, j))
#             player_graph[i][j] = 1
#             fire_graph[i][j] = 0
#         elif graph[i][j] == 'F':
#             fire.append((i, j))
#             fire_graph[i][j] = 1
#         elif graph[i][j] == '.':
#             player_graph[i][j] = 0
#             fire_graph[i][j] = 0

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# def bfs1():
#     q = deque(player)
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if player_graph[nx][ny] == 0:
#                     player_graph[nx][ny] = player_graph[x][y] + 1
#                     q.append((nx, ny))

# def bfs2():
#     q = deque(fire)
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if fire_graph[nx][ny] == 0:
#                     fire_graph[nx][ny] = fire_graph[x][y] + 1
#                     q.append((nx, ny))

# bfs1()
# bfs2()
# result = []
# for i in range(n):
#     for j in range(m):
#         if i == 0 or i == n-1 or j == 0 or j == m-1:
#             if graph[i][j] == '.' or graph[i][j] == 'J':
#                 if player_graph[i][j] < fire_graph[i][j]:
#                     result.append(player_graph[i][j])

# if result:
#     print(min(result))
# else:
#     print('IMPOSSIBLE') # 71%에서 틀림

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))

player = []
fire = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'J':
            player.append((i, j))
        elif graph[i][j] == 'F':
            fire.append((i, j))
            graph[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
escape = [[-1]*m for _ in range(n)]
def bfs():
    q = deque(fire)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'J' or graph[nx][ny] == '.':
                    graph[nx][ny] = graph[x][y] + 1

    q = deque(player)
    escape[player[0][0]][player[0][1]] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != '#':
                    if graph[nx][ny] > escape[x][y] + 1:
                        escape[nx][ny] = escape[x][y] + 1


bfs()
result = []
for i in range(n):
    for j in range(m):
        if escape[i][j] != -1:
            result.append(escape[i][j])

if result:
    print(min(result))
else:
    print('IMPOSSIBLE')