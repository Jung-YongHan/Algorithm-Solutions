# 1976
# �и������� �̿��Ͽ� Ǭ ����
# ��ȹ�� �ִ� ��ε��� Ž���Ͽ� union���ص�, �ٽ� �ѹ� i��° ��ο� i+1��° ��θ� ���Ͽ�
# ���μ� �������� Ȯ��

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
n = int(input())
m = int(input())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 1:
            graph[i].append(j+1)

plan = list(map(int, input().split()))
def topology():
    for a in plan:
        for b in graph[a]:
            if find_parent(parent, a) != find_parent(parent, b):
                union_parent(parent, a, b)
    
    for i in range(m-1):
        if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
            return False
    return True
if topology():
    print("YES")
else:
    print("NO")