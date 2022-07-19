n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
arr = [0]*m
def func(k, st):
    if k == m:
        print(*arr); return
    for i in range(st, n):
        arr[k] = nums[i]
        func(k+1, i+1)
func(0, 0)
