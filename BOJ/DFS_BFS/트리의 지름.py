# 각 노드가 갖는 가중치가 2개 이상이라면 부모노드
# 각 부모노드에서 DFS를 이용하여 가중치의 합이 가장 큰 것이 트리의 지름
# n = int(input())
# graph = [[] for _ in range(n+1)]
# for i in range(n-1):
#     a, b, cost = map(int, input().split())
#     graph[a].append((b, cost))

# parent_node = [] # 부모노드들만 추가
# for i in range(1, n+1):
#     if len(graph[i]) >= 2: # 자식 노드가 2개 이상인 경우만 포함.
#         parent_node.append(i)

# result = []
# count = 0
# def dfs(a):
#     global count
#     for b, cost in graph[a]:
#         count += cost
#         dfs(b)

# for i in range(len(parent_node)):
#     dfs(parent_node[i])
#     result.append(count)
#     count = 0
# print(max(result))

#----------------------------------------------------
# 자식 노드를 펼치는 것이므로 간선을 반대로 한 후 다시 풀어 볼 것