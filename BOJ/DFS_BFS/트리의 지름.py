# �� ��尡 ���� ����ġ�� 2�� �̻��̶�� �θ���
# �� �θ��忡�� DFS�� �̿��Ͽ� ����ġ�� ���� ���� ū ���� Ʈ���� ����
# n = int(input())
# graph = [[] for _ in range(n+1)]
# for i in range(n-1):
#     a, b, cost = map(int, input().split())
#     graph[a].append((b, cost))

# parent_node = [] # �θ���鸸 �߰�
# for i in range(1, n+1):
#     if len(graph[i]) >= 2: # �ڽ� ��尡 2�� �̻��� ��츸 ����.
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
# �ڽ� ��带 ��ġ�� ���̹Ƿ� ������ �ݴ�� �� �� �ٽ� Ǯ�� �� ��