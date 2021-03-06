# 1012
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, arr):
    q = deque([(x, y)])
    if arr[x][y] == 1:
        arr[x][y] = 0
        while q:
            now_x, now_y = q.popleft()
            for i in range(4):
                nx = now_x + dx[i]
                ny = now_y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == 1:
                        q.append((nx, ny))
                        arr[nx][ny] = 0
        return True
    return False

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    array = [[0] * m for _ in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        array[b][a] = 1

    result = 0
    for j in range(n):
        for k in range(m):
            if bfs(j, k, array):
                result += 1
    print(result)
