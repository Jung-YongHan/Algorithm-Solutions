# 1261
# 0, 1 BFS�� �̿��Ͽ� Ǭ ����
# �̷� ã��� ������ ���������� ���� �μ��� ���� ����ġ�� �ٰԵ�.
# �̹� �湮�� ���� �湮�� �ʿ䰡 ������ a->0, a->1�� �� ���� ����ġ�� �ٸ�
# ���� �μ��� ���� ��ǥ�� ���� �� append�� ����ϰ�
# 0���� �̵��� �� ���� ��ǥ�� �ִ´ٸ� appendleft�� ����Ͽ�
# 0���� �̵� �� �켱������ bfs�� ������ �� �ֵ��� �˰����� ����

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