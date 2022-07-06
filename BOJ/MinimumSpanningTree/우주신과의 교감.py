# 1774
import math
import sys
input = sys.stdin.readline

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

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

array = []
graph = [[] for _ in range(n+1)]
for i in range(n):
    x, y = map(int, input().split())
    array.append((x, y))

for i in range(n):
    x1, y1 = array[i]
    index = 0
    while index < n:
        x2, y2 = array[index]
        if index != i:
            dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            graph[i+1].append((index+1, dist))
        index += 1

for i in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

edges = []
for i in range(1, n+1):
    a = i
    for j in graph[i]:
        b, weight = j
        edges.append((weight, a, b))
edges.sort()

result = 0
for edge in edges:
    weight, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += weight

print(f'{result:.2f}')