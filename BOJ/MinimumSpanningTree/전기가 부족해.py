# 1042
# �����ҿ��� ������ ���޵Ǳ⿡ �����Ҹ� �θ���� ����� ���Ͽ�
# �������� parent[x] ���� 0���� �������� union �ÿ� �׻� �θ��尡
# �ǰ� ���� ��� ������ �θ��尡 0�̵Ǹ� ��� ���ÿ�
# ���� ������ �Ǿ��ٴ� ���̹Ƿ� ���� �� ũ�罺Į �˰��� ����

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
    