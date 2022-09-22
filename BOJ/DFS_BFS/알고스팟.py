# 1261
# 0, 1 BFS를 이용하여 푼 문제
# 미로 찾기와 동일한 문제이지만 벽을 부수는 데에 가중치가 붙게됨.
# 이미 방문한 곳은 방문할 필요가 없으며 a->0, a->1로 갈 때의 가중치가 다름
# 벽을 부수고 덱에 좌표를 넣을 때 append를 사용하고
# 0으로 이동할 때 덱에 좌표를 넣는다면 appendleft를 사용하여
# 0으로 이동 시 우선적으로 bfs를 실행할 수 있도록 알고리즘을 설계

from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
q.append([0, 0])
visited[0][0] = True
while q:
    x, y = q.popleft()
    if x == n-1 and y == m-1:
        print(graph[x][y])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y]
                q.appendleft([nx, ny])
            elif not visited[nx][ny] and graph[nx][ny] != 0:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])