# 특정한 최단 경로
# 해당 문제는 간선의 개수가 0일 때의 예외처리를 해주어야하는 문제
# 간선이 0인 경우 가중치의 합이 INF * 노드 수 만큼의 결과가 나올 수 있어,
# 출력 시에 INF값 보다 작은 값일 때 출력해야 정답을 받는다 (INF가 아닐 때 출력 시에 오답)
import heapq
import sys
input = sys.stdin.readline
v, e = map(int, input().split())
INF = int(1e7)
graph = [[] for _ in range(v+1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

def dijkstra(start):
    q = []
    distance = [INF] * (v + 1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

a = dijkstra(1)
b = dijkstra(v1)
c = dijkstra(v2)

result = min(a[v1] + b[v2] + c[v], a[v2] + c[v1] + b[v])
if result < INF:
    print(result)
else:
    print(-1)