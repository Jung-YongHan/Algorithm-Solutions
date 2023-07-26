from collections import deque
from copy import deepcopy

n = int(input())
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
cost = [0]*(n+1)
for i in range(n):
    oper = list(map(int, input().split()))
    cost[i] = oper[0]
    for j in oper[1:-1]:
        indegree[i] += 1
        graph[j].append(i)

def topology_sort():
    result = deepcopy(cost)
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+cost[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
            