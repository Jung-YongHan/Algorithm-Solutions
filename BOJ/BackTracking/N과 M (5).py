n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
arr = [0]*m
visited = [False]*(max(nums)+1)
def func(k):
    if k == m:
        print(*arr); return
    for i in nums:
        if not visited[i]:
            arr[k] = i
            visited[i] = True
            func(k+1)
            visited[i] = False
func(0)
