from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque([(0, 0)])
arr[0][0] = 0
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1
print(arr[n-1][m-1]+1)