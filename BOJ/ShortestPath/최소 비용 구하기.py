# 1916
import sys
import heapq
input = sys.stdin.readline
v = int(input())
e = int(input())
graph = [[] for _ in range(v+1)]
INF = int(1e9)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

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
            cost = distance[now] + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)
print(distance[end])