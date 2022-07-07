from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, count):
    q = deque([(x, y)])
    graph[x][y] = 0
    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))
                    count += 1
    return count + 1 # 자기 자신 포함

maximum = 0
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            r = bfs(i, j, 0)
            if r is not None:
                maximum = max(r, maximum)
                result += 1
print(result)
print(maximum)
