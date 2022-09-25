# 2623
from collections import deque

n, m = map(int, input().split())
arr = []
for i in range(m):
    arr.append(list(map(int, input().split()))[1:])

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for i in range(m):
    for j in range(1, len(arr[i])):
        a, b = arr[i][j-1], arr[i][j]
        graph[a].append(b)
        indegree[b] += 1

result = []
def topology():
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            result.append(i)    

    while q:
        now = q.popleft()
        for j in graph[now]:
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)
                result.append(j)
topology()

available = True
for i in range(n):
    if indegree[i] >= 1:
        available = False

if available:
    for i in range(n):
        print(result[i])
else:
    print(0)


