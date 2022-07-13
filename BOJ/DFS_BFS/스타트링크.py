# 5014
from collections import deque

# 총 f층, 시작 s층, 목표 g층, 위로 u층, 아래로 d층
f, s, g, u, d = map(int, input().split())

array = [-1] * 1000001
array[s] = 0
def bfs():
    q = deque([s])
    while q:
        now = q.popleft()
        if now == g:
            return array[now]
        for x in [now+u, now-d]:
            if x <= 0 or x > f:
                continue
            if array[x] == -1:
                array[x] = array[now] + 1
                q.append(x)
    return 'use the stairs'
print(bfs())

