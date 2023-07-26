# 1389

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((1, b))
    graph[b].append((1, a))
def dijkstra(start):
    distance = [INF]*(n+1)
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))

    return sum(distance[1:])

min_result = INF
min_index = 1
for i in range(1, n+1):
    result = dijkstra(i)
    if result < min_result:
        min_result = result
        min_index = i

print(min_index)