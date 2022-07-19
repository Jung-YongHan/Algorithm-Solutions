n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
arr = [0]*m
def func(k):
    if k == m:
        print(*arr); return
    if k == 0:
        start = 0
    else:
        start = nums.index(arr[k-1]) + 1
    for i in nums[start:]:
        arr[k] = i
        func(k+1)

func(0)
