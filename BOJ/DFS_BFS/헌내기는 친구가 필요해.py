# 21736

import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
array = [list(input()) for _ in range(n)]
start = [(i, j) for i in range(n) for j in range(m) if array[i][j] == 'I']
visited = [[False]*m for _ in range(n)]

result = 0

q = deque([(start[0][0], start[0][1])])
visited[start[0][0]][start[0][1]] = True
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not visited[nx][ny] and array[nx][ny] != 'X':
                q.append((nx, ny))
                visited[nx][ny] = True
                if array[nx][ny] == 'P':
                    result += 1
print(result) if result else print("TT")
