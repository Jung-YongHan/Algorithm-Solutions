# 1042
# 발전소에서 전력이 공급되기에 발전소를 부모노드로 만들기 위하여
# 발전소의 parent[x] 값을 0으로 고정시켜 union 시에 항상 부모노드가
# 되게 만들어서 모든 노드들의 부모노드가 0이되면 모든 도시에
# 전력 공급이 되었다는 뜻이므로 정렬 후 크루스칼 알고리즘 적용

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m, k = map(int, input().split())
power = list(map(int, input().split()))

parent = [0] * (n+1)
for i in range(1, n+1):
    if i not in power:
        parent[i] = i

edges = []
for i in range(m):
    u, v, cost = map(int, input().split())
    edges.append((cost, u, v))
edges.sort()

result = 0
for edge in edges:
    cost, u, v = edge
    if find_parent(parent, u) != find_parent(parent, v):
        union_parent(parent, u, v)
        result += cost
print(result)
    