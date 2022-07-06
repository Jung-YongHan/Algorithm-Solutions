# 2178
from collections import deque

def bfs(arr):
    q = deque([(0, 0)])
    arr[0][0] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = arr[x][y] + 1
                    q.append((nx, ny))

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs(array)
print(array[n-1][m-1] + 1)