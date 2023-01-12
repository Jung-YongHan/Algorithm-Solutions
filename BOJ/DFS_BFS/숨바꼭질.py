from collections import deque

n, k = map(int, input().split())
arr = [-1]*(100001)
arr[n] = 0
q = deque([n])
while True:
    x = q.popleft()
    if x == k:
        print(arr[k])
        break
    for i in [x-1, x+1, 2*x]:
        if 0<=i<=100000 and arr[i]==-1:
            q.append(i)
            arr[i] = arr[x]+1