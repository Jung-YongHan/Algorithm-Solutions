# 요세푸스 문제 0
from collections import deque
n,k=map(int,input().split())
t = deque()
result = []
for i in range(1, n+1):
    t.append(i)
while len(t) > 0:
    for i in range(k-1):
        t.append(t.popleft())
    result.append(t.popleft())
print('<',end='')
for j in range(0, n):
    if j == n-1:
        print(f'{result[j]}>')
    else:
        print(f'{result[j]},',end=' ')