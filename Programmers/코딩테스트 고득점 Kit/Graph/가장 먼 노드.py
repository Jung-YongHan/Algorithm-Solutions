from collections import deque  

def solution(n, edge):
    distance = [0] * (n+1)
    visited = [False] * (n+1)
    
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque([1])
    visited[1] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
    
    distance.sort()
    answer = distance.count(distance[-1])
    return answer