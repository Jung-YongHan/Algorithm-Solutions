# 최단경로
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a에서 b로가는 간선의 가중치 c
distance = [INF] * (v+1)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in distance[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)