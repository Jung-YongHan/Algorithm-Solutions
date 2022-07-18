n, m = map(int, input().split())
arr = [0]*m
visited = [False] * (n+1)
def func(k):
    if k == m:
        print(*arr)
        return
    start = 1
    if k != 0: start = arr[k-1] + 1
    for i in range(start, n+1):
        if not visited[i]:
            arr[k] = i
            visited[i] = True
            func(k+1)
            visited[i] = False   
func(0)