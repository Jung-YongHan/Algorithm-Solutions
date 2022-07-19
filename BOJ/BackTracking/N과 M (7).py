n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
arr = [0]*m
def func(k):
    if k == m:
        print(*arr); return
    for i in nums:
        arr[k] = i
        func(k+1)
func(0)