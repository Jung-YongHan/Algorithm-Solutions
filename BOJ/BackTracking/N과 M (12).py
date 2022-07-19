n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
arr = [0]*m
def func(k, st):
    if k == m:
        print(*arr); return
    tmp = 0
    for i in range(st, n):
        if tmp != nums[i]:
            arr[k] = nums[i]
            tmp = arr[k]
            func(k+1, i)
func(0, 0)