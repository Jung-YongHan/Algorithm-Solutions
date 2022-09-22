# 4485
# 각 도둑루비를 가중치로 계산하여 다익스트라 알고리즘을 사용한 문제
import sys
import heapq
input = sys.stdin.readline

test = 1
INF = int(1e9)
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    cost = [[INF]*n for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dijkstra(x, y):
        pq = []
        heapq.heappush(pq, (graph[x][y], x, y)) # cost, x, y 좌표
        while pq:
            curr_cost, curr_x, curr_y = heapq.heappop(pq)
            if cost[curr_x][curr_y] < curr_cost:
                continue
            for i in range(4):
                nx = curr_x + dx[i]
                ny = curr_y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    ncost = graph[nx][ny]
                    if ncost + curr_cost < cost[nx][ny]:
                        heapq.heappush(pq, (ncost + curr_cost, nx, ny))
                        cost[nx][ny] = curr_cost + ncost
        return cost[n-1][n-1]

    answer = dijkstra(0, 0)
    print(f'Problem {test}: {answer}')
    test += 1