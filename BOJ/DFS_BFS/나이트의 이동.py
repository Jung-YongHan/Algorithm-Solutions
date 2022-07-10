# 7562
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -1, 1, 1, -2, -2, 2, 2]
dy = [-2, 2, -2, 2, -1, 1, -1, 1]

for i in range(int(input())):
    l = int(input())
    q = deque()
    q.append(list(map(int, input().split())))
    target_x, target_y = map(int, input().split())
    graph = [[0]*l for _ in range(l)]

    while q:
        x, y = q.popleft()
        if x == target_x and y == target_y:
            print(graph[x][y])
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))