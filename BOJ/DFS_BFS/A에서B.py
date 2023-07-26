# 16953
from collections import deque

a, b = map(int, input().split())
d = dict()
def bfs(start):
    q = deque()
    q.append((start, 0))
    while q:
        x, count = q.popleft()
        if x == b:
            return count+1
        for i in [x*2, x*10+1]:
            if i <= b:
                if i not in d:
                    q.append((i, count+1))
                    d[i] = 1
    return -1
print(bfs(a))