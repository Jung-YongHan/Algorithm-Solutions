from collections import deque

n, k = map(int, input().split())
INF = int(1e9)
graph = [INF]*100001
graph[n] = 0
def bfs():
    q = deque([n])
    while q:
        x = q.popleft()
        if x == k:
            return graph[x]
        for nx in [x-1, x+1, x*2]:
            if nx < 0 or nx > 100000:
                continue
            if nx == x*2:
                if graph[x] >= graph[nx]:
                    continue
                else:
                    graph[nx] = graph[x]
            else:
                if graph[x] + 1 >= graph[nx]:
                    continue
                else:
                    graph[nx] = graph[x] + 1
            q.append(nx)
print(bfs())