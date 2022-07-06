# 18352 
# 간선 들의 거리가 모두 동일하다면 BFS를 이용하여 최단거리를 구할 수도 있음.

import heapq
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
INF = int(1e9)
distance = [INF] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))


def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    distance[x] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist < distance[now]:
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(x)

result = False
for i in range(1, n + 1):
    if distance[i] == k:
        result = True
        print(i)
if not result:
    print(-1)
